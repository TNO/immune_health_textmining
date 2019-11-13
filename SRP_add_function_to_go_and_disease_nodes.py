## 3B Add function to GO and Disease nodes

def connect_to_graph():
    from py2neo import Graph, Node
    g = Graph("bolt://localhost:7687", auth=("neo4j", "bla"))
    return g

def create_function_go_dict():
    function_go_dict = {}
    with open("C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\aop_go_terms\\3B\\function_to_go.txt","r") as function_go_file:
        for line in function_go_file:
            line=line.rstrip()
            function,go,term = line.split("\t")[0],line.split("\t")[1],line.split("\t")[2]
            go=go.replace(" ","")
            if function not in function_go_dict.keys():
                function_go_dict[function] = set()
            function_go_dict[function].add(go)
    return function_go_dict

def create_function_disease_dict():
    function_disease_dict = {}
    with open("C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\aop_go_terms\\3B\\function_to_disease.txt","r") as function_disease_file:
        for line in function_disease_file:
            line=line.rstrip()
            function,disease,term = line.split("\t")[0],line.split("\t")[1],line.split("\t")[2]

            if function not in function_disease_dict.keys():
                function_disease_dict[function] = set()
            function_disease_dict[function].add(disease)
    return function_disease_dict

def get_connected_disease_of_go_neo4j(go):
    g = connect_to_graph()
    result = g.run('MATCH (g)--(d:Disease) WHERE g.GO_term = "'+go+'" AND (g:GOslim OR g:GO) return d')
    data = result.data()
    disease_name_list = []
    for disease in data:
        name = str(disease['d']['name'])
        disease_name_list.append(name)

    return disease_name_list

def add_function_label_to_disease(function_go_dict):
    g = connect_to_graph()
    for function in function_go_dict:
        print(function)
        disease_set = set()
        for go in function_go_dict[function]:
            temp_disease_list = get_connected_disease_of_go_neo4j(go)
            [ disease_set.add(d) for d in temp_disease_list ]
        print(len(disease_set))
        for disease in disease_set:
            node = g.nodes.match("Disease", name=disease).first()

            if node is not None:
                node.add_label(function)
                node.update()
                g.push(node)

def create_function_node(function_go_dict):
    from py2neo import Graph, Node
    g = connect_to_graph()
    for function in function_go_dict:
        node = Node("Gut_Function", name=function+'_gut_function')
        g.merge(node, "Gut_Function", "name")

def get_processes_neo4j(go):
    g = connect_to_graph()
    result = g.run('MATCH (g) WHERE g.GO_term = "'+go+'" AND (g:GOslim OR g:GO) return g')
    data = result.data()
    go_name_list = []
    for d in data:
        name = str(d['g']['GO_term'])
        go_name_list.append(name)

    return go_name_list

def create_relationship_endpoint_disease(function_go_dict, function, found_go,disease_go_dict):
    from py2neo import Relationship
    g = connect_to_graph()
    for disease in disease_go_dict:
        n = len(function_go_dict[function]) # N total
        m = len(found_go) # Matched
        c = len(disease_go_dict[disease]) # Connected
        inference = ((c*(m/n))/n)

        disease_node = g.nodes.match("Disease", name=disease).first()
        function_node = g.nodes.match("Gut_Function", name=function+'_gut_function').first()

        relation = Relationship(disease_node, 'gut_function_inference', function_node, inference_score=inference)

        g.merge(relation)

def create_relationship_endpoint_go(function, found_go):
    from py2neo import Relationship
    g = connect_to_graph()

    for go in found_go:
        go_node = g.nodes.match("GO", GO_term=go).first()
        if go_node is None:
            go_node = g.nodes.match("GOslim", GO_term=go).first()
        if go_node is not None:
            function_node = g.nodes.match("Gut_Function", name=function+'_gut_function').first()
            relation = Relationship(go_node, 'gut_function_inference', function_node)
            g.merge(relation)

def find_go_in_network(function_go_dict):

    from py2neo import Graph, Node, Relationship
    for function in function_go_dict:
        print(function)
        disease_set = set()
        found_go = set()
        disease_go_dict = {}
        print("len go:",len(function_go_dict[function]))
        # Find available GO terms in network
        for go in function_go_dict[function]:
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
        create_relationship_endpoint_disease(function_go_dict, function, found_go,disease_go_dict)
        create_relationship_endpoint_go(function, found_go)



def find_disease_in_network(function_disease_dict):
    from py2neo import Graph, Node, Relationship

    for function in function_disease_dict:
        for disease in function_disease_dict[function]:
            create_relationship_function_disease(function, disease)

def create_relationship_function_disease(function, disease):
    from py2neo import Relationship

    g = connect_to_graph()

    disease_node = g.nodes.match("Disease", name=disease).first()

    if disease_node is not None:
        function_node = g.nodes.match("Gut_Function", name=function+'_gut_function').first()
        relation = Relationship(disease_node, 'gut_function_inference', function_node)
        g.merge(relation)

def gut_function_main():
    function_go_dict = create_function_go_dict()
    function_disease_dict = create_function_disease_dict()
    create_function_node(function_go_dict)

    find_go_in_network(function_go_dict)

    find_disease_in_network(function_disease_dict)

gut_function_main()