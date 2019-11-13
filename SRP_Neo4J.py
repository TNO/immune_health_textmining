def import_files():
#     # Birth
#     filepath_dict = {
#         "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\birth\\network_3A_Birth_denoised default edge.csv",
#         "node_filepath" :  "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\birth\\network_3A_Birth_denoised default node.csv",
#         "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\genemania\\3A\\Human\\Birth\\network_3A_Birth_noise default node.csv",
#         "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO_3A_Birth.csv",
#         "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3A_Birth.csv"
#     }
#     # EG Period
#     filepath_dict = {
#         "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\eg_period\\network_3A_ep_period_denoised default edge.csv",
#         "node_filepath" :  "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\eg_period\\network_3A_ep_period_denoised default node.csv",
#         "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\genemania\\3A\\Human\\Early_gestational_period\\network_3A_EP_period_noise default node.csv",
#         "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO_3A_EG_period.csv",
#         "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3A_EG_period.csv"
#     }
#     # Infant
#     filepath_dict = {
#         "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\infant\\network_3A_infant_denoised default edge.csv",
#         "node_filepath" :  "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\infant\\network_3A_infant_denoised default node.csv",
#         "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\genemania\\3A\\Human\\Infant\\network_3A_Infant_noise default node.csv",
#         "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO_3A_Infant.csv",
#         "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3A_Infant.csv"
#     }
#     # LG Period
#     filepath_dict = {
#         "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\lg_period\\network_3A_lg_period_denoised default edge.csv",
#         "node_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\lg_period\\network_3A_lg_period_denoised default node.csv",
#         "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\genemania\\3A\\Human\\Late_gestational_period\\network_3A_LG_period_noise default node.csv",
#         "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO_3A_LG_period.csv",
#         "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3A_LG_period.csv"
#     }
#     # MG Period
#     filepath_dict = {
#         "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\mg_period\\network_3A_mg_period_denoised default edge.csv",
#         "node_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\mg_period\\network_3A_mg_period_denoised default node.csv",
#         "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\genemania\\3A\\Human\\Mid_gestational_period\\network_3A_MG_period_noise default node.csv",
#         "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO_3A_MG_period.csv",
#         "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3A_MG_period.csv"
#     }
#     # Newborn
#     filepath_dict = {
#         "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\newborn\\network_3A_newborn_denoised default edge.csv",
#         "node_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3A\\newborn\\network_3A_newborn_denoised default node.csv",
#         "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\genemania\\3A\\Human\\Newborn\\network_3A_Newborn_noise default node.csv",
#         "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO_3A_Newborn.csv",
#         "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3A_Newborn.csv"
#     }
    # 3B
    filepath_dict = {
        "edge_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3B\\network_3B_denoised default edge.csv",
        "node_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3B\\network_3B_denoised default node.csv",
        "noise_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\3B\\network_3B_noise default node.csv",
        "disgenet_filepath" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\disgenet\\Gene_Disease_relation_MESH_DO_HPO23B.csv",
        "venny_file_path" : "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\venny_3B\\venny_genes_1296.txt",
        "go_goslim_filepath": "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\go\\Gene2GOandGOslim1_3B.csv"
    }
    
    return filepath_dict

def get_node_info():
    node_dict = {}
    noise_node_dict = {}
    
    default_header = ["SUID","bel.function","ChEBI","FPLX","GO","HGNC","HMDB","InterPro","MESH","name","Pfam","PubChem","selected","shared name","type","UniProt"]
    
    node_filepath = import_files()['node_filepath']
    print(node_filepath)
    noise_filepath = import_files()['noise_filepath']
    print(noise_filepath)
    
    with open(node_filepath) as nodefile:
        # Create header list
        header = nodefile.readline().replace('"', '').rstrip().split(',')    
        for row in nodefile:
            temp_dict = {}
            row=row.replace('"', '').rstrip().split(',')
            for key, value in zip(header, row):
                if value != '':
                    temp_dict[key] = str(value)                
            node_dict[ temp_dict['name'] ] = temp_dict
            
    if noise_filepath != "":
        with open(noise_filepath) as noisefile:
            # Create header list
            noise_header = noisefile.readline().replace('"', '').rstrip().split(',')    
            for row in noisefile:
                temp_noise_dict = {}
                row=row.replace('"', '').rstrip().split(',')
                for key, value in zip(noise_header, row):
                    if value != '':
                        temp_noise_dict[key] = str(value)
                        
                
                # Loop through default header list and add key = "" if not present
                for head in default_header:
                    # if header not in properties, add to properties
                    if head not in temp_noise_dict.keys():
                        temp_noise_dict[head] = ""
                        
                        
                        
                noise_node_dict[ temp_noise_dict['name'] ] = temp_noise_dict
    
            
    return node_dict, header, noise_node_dict

def connect_to_graph():
    from py2neo import Graph
    g = Graph("bolt://localhost:7687", auth=("neo4j", "bla"))
    
    return g

def create_relationship(indra_dict, node_dict, header, gMerge, gUpdate, g, node_a, node_b):
    from py2neo import Node, Relationship
    
    try:
        # Create node
        a = Node("INDRA", name=indra_dict[node_a]["name"])
        # Loop through properties
        for prop_a in node_dict[indra_dict[node_a]["name"]]:
            #Check if type == other
            if node_dict[indra_dict[node_a]["name"]]['type'] == 'other':
                #Check if other-type has more keys
                if any(key in node_dict[indra_dict[node_a]["name"]] for key in ('bel.function','ChEBI','FPLX','GO','HGNC','HMDB','InterPro','MESH','Pfam','PubChem','UniProt')): 
                    pass
                else:
                    gMerge = False
                    gUpdate = False
                    continue
            # Loop through header list
            for head in header:
                # if header not in properties, add to properties
                if head not in node_dict[indra_dict[node_a]["name"]].keys():
                    a[head] = ""
            a[prop_a] = node_dict[indra_dict[node_a]["name"]][prop_a]
            if gUpdate:
                # Update original properties to Neo4j
                a.add_label(node_dict[indra_dict[node_a]["name"]]['type'])
                a.update()
    except KeyError as e:
        print('KeyError in node A - reason "%s"' % str(e))
        gMerge = False
        
    try:
        # Add node properties
        b = Node("INDRA", name=indra_dict[node_b]["name"])
        for prop_b in node_dict[indra_dict[node_b]["name"]]:
            #Check if type == other
            if node_dict[indra_dict[node_b]["name"]]['type'] == 'other':
                #Check if other-type has more keys
                if any(key in node_dict[indra_dict[node_b]["name"]] for key in ('bel.function','ChEBI','FPLX','GO','HGNC','HMDB','InterPro','MESH','Pfam','PubChem','UniProt')): 
                    pass
                else:
                    gUpdate = False
                    gMerge = False
                    continue
            for head in header:
                # if header not in properties, add to properties
                if head not in node_dict[indra_dict[node_b]["name"]].keys():
                    b[head] = ""
            b[prop_b] = node_dict[indra_dict[node_b]["name"]][prop_b]
            if gUpdate:
                b.add_label(node_dict[indra_dict[node_b]["name"]]['type'])
                b.update()
                
    except KeyError as e:
        print('KeyError in node B - reason "%s"' % str(e))
        gMerge = False
        
    if gMerge:
        # Add edge and properties
        relation = Relationship(a,indra_dict["type"],b,evidence=indra_dict["evidence"][0]["text"],belief=indra_dict["belief"])
        # Merge nodes with edge
        g.merge(relation, "INDRA", "name")

def create_complex_relationship(indra_dict, node_dict, header, gMerge, gUpdate, g):
    from py2neo import Node, Relationship
    
    try:
        # Create node
        a = Node("INDRA", name=indra_dict['members'][0]["name"])
        # Loop through properties
        for prop_a in node_dict[indra_dict['members'][0]["name"]]:
            #Check if type == other
            if node_dict[indra_dict['members'][0]["name"]]['type'] == 'other':
                #Check if other-type has more keys
                if any(key in node_dict[indra_dict['members'][0]["name"]] for key in ('bel.function','ChEBI','FPLX','GO','HGNC','HMDB','InterPro','MESH','Pfam','PubChem','UniProt')): 
                    pass
                else:
                    gMerge = False
                    gUpdate = False
                    continue
            # Loop through header list
            for head in header:
                # if header not in properties, add to properties
                if head not in node_dict[indra_dict['members'][0]["name"]].keys():
                    a[head] = ""
            a[prop_a] = node_dict[indra_dict['members'][0]["name"]][prop_a]
            if gUpdate:
                # Update original properties to Neo4j
                a.add_label(node_dict[indra_dict['members'][0]["name"]]['type'])
                a.update()
    except KeyError as e:
        print('KeyError in node A - reason "%s"' % str(e))
        gMerge = False
        
    try:
        # Add node properties
        b = Node("INDRA", name=indra_dict['members'][1]["name"])
        for prop_b in node_dict[indra_dict['members'][1]["name"]]:
            #Check if type == other
            if node_dict[indra_dict['members'][1]["name"]]['type'] == 'other':
                #Check if other-type has more keys
                if any(key in node_dict[indra_dict['members'][1]["name"]] for key in ('bel.function','ChEBI','FPLX','GO','HGNC','HMDB','InterPro','MESH','Pfam','PubChem','UniProt')): 
                    pass
                else:
                    gUpdate = False
                    gMerge = False
                    continue
            for head in header:
                # if header not in properties, add to properties
                if head not in node_dict[indra_dict['members'][1]["name"]].keys():
                    b[head] = ""
            b[prop_b] = node_dict[indra_dict['members'][1]["name"]][prop_b]
            if gUpdate:
                b.add_label(node_dict[indra_dict['members'][1]["name"]]['type'])
                b.update()
                
    except KeyError as e:
        print('KeyError in node B - reason "%s"' % str(e))
        gMerge = False
    
        
    if gMerge:
            # Add edge and properties
            relation = Relationship(a,indra_dict["type"],b,evidence=indra_dict["evidence"][0]["text"],belief=indra_dict["belief"])
            # Merge nodes with edge
            g.merge(relation, "INDRA", "name")

def main():
    import csv
    import json
    
    #Set to True when only importing nodes
#     gNodesOnly = True
    
    edge_filepath = import_files()['edge_filepath']
    print(edge_filepath)
    
    g = connect_to_graph()
    node_dict, header, noise_node_dict = get_node_info()

    with open(edge_filepath, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for line in csv_reader:
            
            indra_json_raw = line[1]
            indra_dict = json.loads(indra_json_raw)
            gUpdate = True
            gMerge = True
            if indra_dict["type"] in ["IncreaseAmount","DecreaseAmount","Activation","Inhibition"]:
                node_a = "subj"
                node_b = "obj"
                create_relationship(indra_dict, node_dict, header, gMerge, gUpdate, g, node_a, node_b)

            elif indra_dict["type"] in ["Complex"]:
                create_complex_relationship(indra_dict, node_dict, header, gMerge, gUpdate, g)
#             elif indra_dict["type"] in ["Methylation","Demethylation","Acetylation","Deacetylation","Phosphorylation","Dephosphorylation","Hydroxylation","Dehydroxylation","Glycosylation","Ubiquitination"]:
            else:
                node_a = "sub"
                node_b = "enz"
                create_relationship(indra_dict, node_dict, header, gMerge, gUpdate, g, node_a, node_b)

def add_noise_nodes():
    from py2neo import Node
    
    g = connect_to_graph()
    
    node_dict, header, noise_node_dict = get_node_info()
    
    for noise in noise_node_dict:
        a = Node("INDRA", name=noise_node_dict[noise]['name'])
        node = g.nodes.match("INDRA", name=noise).first()
        for key in noise_node_dict[noise]:
            a[key] = noise_node_dict[noise][key]
            a.add_label(noise_node_dict[noise]['type'])
            a.update()
        if not node:
#             print('Adding',noise,'to the Graph')
            g.merge(a,"INDRA","name")

main()
add_noise_nodes()

def add_diseases():
    from py2neo import Node, Relationship
    
    g = connect_to_graph()
    
    disgenet_filepath = import_files()['disgenet_filepath']
    
    data = {}
    keyList = ['description','link','genelist','DO','HPO','MSH']
    
    with open(disgenet_filepath,"r") as disgenet_file:
        disgenet_file.readline()
        for line in disgenet_file:
            line=line.rstrip().replace('"', '')
            disease,description,link,genelist,vocabulary,code = line.split('\t')[0],line.split('\t')[1],line.split('\t')[2],line.split('\t')[10],line.split('\t')[12],line.split('\t')[13]
            
            if disease not in data.keys():
                data[disease] = {}
                data[disease] = dict((key, []) for key in keyList)
                
                if vocabulary == 'DO':
                    data[disease]['DO'] = [code]
                if vocabulary == 'HPO':
                    data[disease]['HPO'] = [code]
                if vocabulary == 'MSH':
                    data[disease]['MSH'] = [code]
                data[disease]['description'] = description
                data[disease]['link'] = link
                data[disease]['genelist'] = genelist.split(';')
                
            else:
                if vocabulary == 'DO':
                    data[disease]['DO'].append(code)
                if vocabulary == 'HPO':
                    data[disease]['HPO'].append(code)
                if vocabulary == 'MSH':
                    data[disease]['MSH'].append(code)

    #DisGeNET only  
    for disease in data:
        d = Node("Disease", name=data[disease]['description'], link=data[disease]['link'], diseaseID=disease, DO=data[disease]['DO'], HPO=data[disease]['HPO'], MSH=data[disease]['MSH'])
        g.merge(d, "Disease", "name")
        
        for gene in data[disease]['genelist']:
            indra_node = g.nodes.match("INDRA", name=gene).first()
            venny_node = g.nodes.match("gene", name=gene).first()
            if indra_node is not None:
                relation = Relationship(indra_node,'DisGeNET_connection',d)
                g.merge(relation)
            if venny_node is not None:
                relation = Relationship(venny_node,'DisGeNET_connection',d)
                g.merge(relation)
                    
#     #MeSH only
#     for mesh in data[disease]['MSH']:
#         meshNode = Node("MeSH", name=data[disease]['description'], MeSH_ID=data[disease]['MSH'])
#         g.merge(meshNode, "MeSH", "name")

#         for gene in data[disease]['genelist']:
#             node = g.nodes.match("INDRA", name=gene).first()
#             if node is not None:
#                 relation = Relationship(node,'MeSH_connection',meshNode)
#                 g.merge(relation)
add_diseases()

def add_go_and_goslim():
    from py2neo import Node, Relationship
    
    g = connect_to_graph()
    
    go_goslim_filepath = import_files()['go_goslim_filepath']
    
    go_data = {}
    goslim_data = {}
    
    with open(go_goslim_filepath,"r") as go_goslim_file:
        go_goslim_file.readline()
        for line in go_goslim_file:
            line=line.rstrip()
            split_list = line.split('\t')
            goID,gene,goTerm,goslimID,count,percent,goslimTerm = split_list[0],split_list[1],split_list[2],split_list[3],split_list[4],split_list[5],split_list[6]
            
            if goID != 'NA':
                if goID not in go_data.keys():
                    go_data[goID] = {}
                    go_data[goID]['name'] = goTerm
                    go_data[goID]['genes'] = [gene]
                    go_data[goID]['count'] = count
                    go_data[goID]['percent'] = percent
                else:
                    go_data[goID]['genes'].append(gene)
            
            if goslimID != 'NA':
                if goslimID not in goslim_data.keys():
                    goslim_data[goslimID] = {}
                    goslim_data[goslimID]['name'] = goslimTerm
                    goslim_data[goslimID]['genes'] = [gene]
                    goslim_data[goslimID]['count'] = count
                    goslim_data[goslimID]['percent'] = percent
                else:
                    goslim_data[goslimID]['genes'].append(gene)
                    
    for go in go_data:
        goNode = Node("GO", name=go_data[go]['name'], GO_term=go)
        g.merge(goNode, "GO", "name")
        for gene in go_data[go]['genes']:
            indra_node = g.nodes.match("INDRA", name=gene).first()
            venny_node = g.nodes.match("gene", name=gene).first()
            if indra_node is not None:
                relation = Relationship(indra_node,'GO_connection',goNode)
                g.merge(relation)
            if venny_node is not None:
                relation = Relationship(venny_node,'GO_connection',goNode)
                g.merge(relation)
                
                
    for goSlim in goslim_data:
        GOnode = g.nodes.match("GO", GO_term=goSlim).first()
        if GOnode is None:
            goSlimNode = Node("GOslim", name=goslim_data[goSlim]['name'], GO_term=goSlim)
            g.merge(goSlimNode, "GOslim", "name")
            for gene in goslim_data[goSlim]['genes']:
                indra_node = g.nodes.match("INDRA", name=gene).first()
                venny_node = g.nodes.match("gene", name=gene).first()
                if indra_node is not None:
                    
                    relation = Relationship(indra_node,'GO_slim_connection',goSlimNode)
                    g.merge(relation)
                if venny_node is not None:
                    
                    relation = Relationship(venny_node,'GO_slim_connection',goSlimNode)
                    g.merge(relation)
        else:
            print("GO already exists:",goSlim,". Adding label.")
            GOnode.add_label('GOslim')
            GOnode.update()
            g.push(GOnode)
            
            for gene in goslim_data[goSlim]['genes']:
                indra_node = g.nodes.match("INDRA", name=gene).first()
                venny_node = g.nodes.match("gene", name=gene).first()
                if indra_node is not None:
                    
                    relation = Relationship(indra_node,'GO_slim_connection',GOnode)
                    
                    g.merge(relation)
                if venny_node is not None:
                    
                    relation = Relationship(venny_node,'GO_slim_connection',GOnode)
                    g.merge(relation)   
# # Venny genes:
#         goSlimNode = Node("GOslim", name=data[goSlim]['name'], GOslim_term=goSlim)
#         g.merge(goSlimNode, "GOslim", "name")
#         for gene in data[goSlim]['genes']:
#             indra_node = g.nodes.match("INDRA", name=gene).first()
#             venny_node = g.nodes.match("gene", name=gene).first()
#             if indra_node is not None:
#                 teller+=1
#                 relation = Relationship(indra_node,'GO_slim_connection',goSlimNode)
#                 g.merge(relation)
#             if venny_node is not None:
#                 teller+=1
#                 relation = Relationship(venny_node,'GO_slim_connection',goSlimNode)
#                 g.merge(relation)
            
add_go_and_goslim()

def add_venny_genes():
    from py2neo import Node
    
    venny_file_path = import_files()['venny_file_path']
    
    g = connect_to_graph()
    
    gene_dict = {}
    gene_set = set()
    
    with open(venny_file_path,'r') as venny_file:
        venny_file.readline()
        for line in venny_file:
            line=line.rstrip()
            entrez,gene,description = line.split('\t')[0],line.split('\t')[1],line.split('\t')[2].split(' [')[0]
            gene_dict[gene] = {}
            gene_dict[gene]['entrez'] = entrez
            gene_dict[gene]['description'] = description
            
    
    for gene in gene_dict:
        node = g.nodes.match("INDRA", name=gene).first()
        if node is None:
            gene_node = Node("gene", name=gene, entrez=gene_dict[gene]['entrez'], description=gene_dict[gene]['description'])
            g.merge(gene_node, "gene", "name")
        else:
            node.add_label('gene')
            node['entrez'] = entrez
            node.update()
            g.push(node)
    
add_venny_genes()
