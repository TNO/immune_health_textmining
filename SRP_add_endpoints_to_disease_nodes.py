## 3A Add endpoints (AOP's) to Disease nodes
def connect_to_graph():
    from py2neo import Graph, Node
    g = Graph("bolt://localhost:7687", auth=("neo4j", "bla"))
    return g

def create_aop_go_dict():
    aop_go_dict = {}
    with open("C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\aop_go_terms\\aop_go.txt","r") as aop_go_file:
        for line in aop_go_file:
            line=line.rstrip()
            aop,go,term = line.split("\t")[0],line.split("\t")[1],line.split("\t")[2]
            go=go.replace(" ","")
            if aop not in aop_go_dict.keys():
                aop_go_dict[aop] = set()
            else:
                aop_go_dict[aop].add(go)
    return aop_go_dict

def get_connected_disease_of_go_neo4j(go):
    g = connect_to_graph()
    result = g.run('MATCH (g)--(d:Disease) WHERE g.GO_term = "'+go+'" AND (g:GOslim OR g:GO) return d')
    data = result.data()
    disease_name_list = []
    for disease in data:
        name = str(disease['d']['name'])
        disease_name_list.append(name)

    return disease_name_list

def add_aop_label_to_disease(aop_go_dict):
    g = connect_to_graph()
    for aop in aop_go_dict:
        print(aop)
        disease_set = set()
        for go in aop_go_dict[aop]:
            temp_disease_list = get_connected_disease_of_go_neo4j(go)
            [ disease_set.add(d) for d in temp_disease_list ]
        print(len(disease_set))
        for disease in disease_set:
            node = g.nodes.match("Disease", name=disease).first()

            if node is not None:
                node.add_label(aop)
                node.update()
                g.push(node)

def create_aop_node(aop_go_dict):
    from py2neo import Graph, Node
    g = connect_to_graph()
    for aop in aop_go_dict:
        node = Node("ImmuneEndpoint", name=aop+'_immune_endpoint')
        g.merge(node, "ImmuneEndpoint", "name")

def get_processes_neo4j(go):
    g = connect_to_graph()
    result = g.run('MATCH (g) WHERE g.GO_term = "'+go+'" AND (g:GOslim OR g:GO) return g')
    data = result.data()
    go_name_list = []
    for d in data:
        name = str(d['g']['GO_term'])
        go_name_list.append(name)

    return go_name_list

def create_relationship_endpoint_disease(aop_go_dict, aop, found_go,disease_go_dict):
    print("adding endpoint to diseases")
    from py2neo import Relationship
    g = connect_to_graph()
    for disease in disease_go_dict:
        n = len(aop_go_dict[aop]) # N total
        m = len(found_go) # Matched
        c = len(disease_go_dict[disease]) # Connected
        inference = ((c*(m/n))/n)

        disease_node = g.nodes.match("Disease", name=disease).first()
        aop_node = g.nodes.match("ImmuneEndpoint", name=aop+'_immune_endpoint').first()

        relation = Relationship(disease_node, 'endpoint_inference', aop_node, inference_score=inference)

        g.merge(relation)

def create_relationship_endpoint_go(aop, found_go):
    from py2neo import Relationship
    print("adding endpoint to go")
    g = connect_to_graph()

    for go in found_go:
        go_node = g.nodes.match("GO", GO_term=go).first()
        if go_node is None:
            go_node = g.nodes.match("GOslim", GO_term=go).first()
        aop_node = g.nodes.match("ImmuneEndpoint", name=aop+'_immune_endpoint').first()
        relation = Relationship(go_node, 'endpoint_inference', aop_node)
        g.merge(relation)

def find_go_in_network(aop_go_dict):

    from py2neo import Graph, Node, Relationship
    for aop in aop_go_dict:
        print(aop)
        disease_set = set()
        found_go = set()
        disease_go_dict = {}
        print("len go:",len(aop_go_dict[aop]))
        # Find available GO terms in network
        for go in aop_go_dict[aop]:
            go_list = get_processes_neo4j(go)
            [ found_go.add(g) for g in go_list ]

            # Find connected diseases of GO
            temp_disease_list = get_connected_disease_of_go_neo4j(go)
            [ disease_set.add(d) for d in temp_disease_list ]
            # Create dictionary with found GO terms per disease
            for disease in temp_disease_list:
                if disease not in disease_go_dict.keys():
                    disease_go_dict[disease] = set()
                disease_go_dict[disease].add(go)

        # create relationship and calculate inference
        create_relationship_endpoint_disease(aop_go_dict, aop, found_go,disease_go_dict)
        create_relationship_endpoint_go(aop, found_go)


def aop_main():
    aop_go_dict = create_aop_go_dict()
    create_aop_node(aop_go_dict)
    find_go_in_network(aop_go_dict)
aop_main()