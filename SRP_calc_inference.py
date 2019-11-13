#Calculate inference
def export_GOslim():
    from py2neo import Graph, NodeMatcher

    g = connect_to_graph()
    matcher = NodeMatcher(g)
    goslim_list= list(matcher.match("GOslim"))

    return goslim_list


def export_disgenet():
    from py2neo import Graph, NodeMatcher

    g = connect_to_graph()
    matcher = NodeMatcher(g)
    disgenet_list= list(matcher.match("Disease"))

    return disgenet_list

def export_GO():
    from py2neo import Graph, NodeMatcher

    g = connect_to_graph()
    matcher = NodeMatcher(g)
    go_list= list(matcher.match("GO"))

    return go_list

def export_bioprocess():
    from py2neo import Graph, NodeMatcher

    g = connect_to_graph()
    matcher = NodeMatcher(g)
    bioprocess_list= list(matcher.match("bioprocess"))

    return bioprocess_list

def get_connected_proteins(label,name):
    from ast import literal_eval

    g = connect_to_graph()
    proteins_result = g.run('MATCH (n:`'+label+'`)--(p) where n.name = "'+name+'" AND (p:protein OR p:gene) RETURN p')
    proteins_data = proteins_result.data()

    protein_set = set()

    [ protein_set.add(protein['p']['name']) for protein in proteins_data ]
    return protein_set

def calc_inference(period):
    print("Calculating inference scores")
    from py2neo import Relationship
    g = connect_to_graph()

#     print('get disgenet proteins')
    disgenet_list = export_disgenet()
#     print('Size:',len(disgenet_list))
    disgenet_dict = {}
    for disgenet in  disgenet_list:
        disgenet_prot_set = get_connected_proteins("Disease",disgenet['name'])
        disgenet_dict[disgenet] = disgenet_prot_set
    goslim_list = export_GOslim()
    go_list = export_GO()
    bioprocess_list = export_bioprocess()

    with open('C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\inference\\'+period+'_inference.txt','w') as outfile:
        outfile.write('label\tname\tsize\tdisgenet\tsize disgenet\tsize overlap\tinference score\n')

#         print('GOslim')
#         print('Size:',len(goslim_list))
        for goslim in goslim_list:
            goslim_prot_set = get_connected_proteins('GOslim',goslim['name'])
            for disgenet in  disgenet_list:
                disgenet_prot_set = disgenet_dict[disgenet]
                intersection = goslim_prot_set.intersection(disgenet_prot_set)

                if len(intersection) > 0:
                    outfile.write('goslim\t')
                    outfile.write(goslim['name']+'\t')
                    outfile.write(str(len(goslim_prot_set))+'\t')
                    outfile.write(disgenet['name']+'\t')
                    outfile.write(str(len(disgenet_prot_set))+'\t')
                    outfile.write(str(len(intersection))+'\t')
                    inference_score = len(intersection)/len(disgenet_prot_set)
                    outfile.write(str(inference_score)+'\n')

                    relation = Relationship(goslim,'Inference',disgenet,inference_score=inference_score)
                    g.merge(relation)

#         print('GO')
#         print('Size:',len(go_list))
        for go in go_list:
            go_prot_set = get_connected_proteins('GO',go['name'])
            for disgenet in  disgenet_list:
                disgenet_prot_set = disgenet_dict[disgenet]
                intersection = go_prot_set.intersection(disgenet_prot_set)
                if len(intersection) > 0:

                    outfile.write('go\t')
                    outfile.write(go['name']+'\t')
                    outfile.write(str(len(go_prot_set))+'\t')
                    outfile.write(disgenet['name']+'\t')
                    outfile.write(str(len(disgenet_prot_set))+'\t')
                    outfile.write(str(len(intersection))+'\t')
                    inference_score = len(intersection)/len(disgenet_prot_set)
                    outfile.write(str(inference_score)+'\n')

                    relation = Relationship(go,'Inference',disgenet,inference_score=inference_score)
                    g.merge(relation)

#         print('bioprocess')
#         print('Size:',len(bioprocess_list))
        for bioprocess in bioprocess_list:
            bioprocess_prot_set = get_connected_proteins('bioprocess',bioprocess['name'])
            for disgenet in  disgenet_list:
                disgenet_prot_set = disgenet_dict[disgenet]
                intersection = bioprocess_prot_set.intersection(disgenet_prot_set)
                if len(intersection) > 0:
                    outfile.write('bioprocess\t')
                    outfile.write(bioprocess['name']+'\t')
                    outfile.write(str(len(bioprocess_prot_set))+'\t')
                    outfile.write(disgenet['name']+'\t')
                    outfile.write(str(len(disgenet_prot_set))+'\t')
                    outfile.write(str(len(intersection))+'\t')
                    outfile.write(str(len(intersection)/len(disgenet_prot_set))+'\n')
                    inference_score = len(intersection)/len(disgenet_prot_set)
                    outfile.write(str(inference_score)+'\n')

                    relation = Relationship(bioprocess,'Inference',disgenet,inference_score=inference_score)
                    g.merge(relation)