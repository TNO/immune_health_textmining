## Gene prioritization
def connect_to_graph():
    from py2neo import Graph
    g = Graph("bolt://localhost:7687", auth=("neo4j", "bla"))

    return g

def export_disgenet_neo4j():
    from py2neo import Graph, NodeMatcher

    g = connect_to_graph()
    matcher = NodeMatcher(g)
    disgenet_list= list(matcher.match("Disease"))

    return disgenet_list

def get_connected_processes_of_disease_neo4j(disease):
#     print("Get connected processes from disease:",disease)
    from ast import literal_eval

    g = connect_to_graph()
    process_result = g.run('MATCH (d:Disease)--(p) WHERE d.name = "'+disease+'" AND (p:GOslim OR p:bioprocess) return p')
    process_data = process_result.data()

    process_name_list = []
    for process in process_data:
        name = str(process['p']['name'])
        process_name_list.append(name)

    return process_name_list

def get_connected_processes_of_genes_offline(disease,gene_list,disease_process_gene_dict):
    new_process_list = set()
    for gene in gene_list:
        for process in disease_process_gene_dict[disease].keys():
            if gene in disease_process_gene_dict[disease][process]:
                new_process_list.add(process)

    return list(new_process_list)

def get_number_connected_processes_offline(disease,disease_process_gene_dict,total_gene_list):
    gene_process_number_dict = {}

    for gene in total_gene_list:
        count = 0
        for process in disease_process_gene_dict[disease].keys():
            if gene in disease_process_gene_dict[disease][process]:
                count +=1
        gene_process_number_dict[gene] = count

    return gene_process_number_dict


def get_connected_proteins_of_process_neo4j(disease,disease_process_gene_dict,process_list):
    g = connect_to_graph()

    for process in process_list:
        proteins_result = g.run('MATCH (bp)--(p) where bp.name = "'+process+'" AND (bp:GOslim OR bp:bioprocess) AND (p:protein OR p:gene) RETURN p')
        proteins_data = proteins_result.data()

        protein_set = set()

        [ protein_set.add(protein['p']['name']) for protein in proteins_data ]

        disease_process_gene_dict[disease][process] = list(protein_set)


    return disease_process_gene_dict

def get_connected_processes_of_protein_neo4j(protein_list):
    g = connect_to_graph()

    total_process_set = set()

    for protein in protein_list:
        process_result = g.run('MATCH (p)--(bp) where p.name = "'+protein+'" AND (bp:GOslim OR bp:bioprocess) AND (p:protein OR p:gene) RETURN bp')
        process_data = process_result.data()

        process_set = set()

        [ process_set.add(process['bp']['name']) for process in process_data ]

        [ total_process_set.add(process) for process in process_set ]


    return list(total_process_set)

def create_gene_list(disease,process_list,disease_process_gene_dict):
    total_gene_list = set()
    for process in process_list:
        gene_list = disease_process_gene_dict[disease][process]
        [ total_gene_list.add(gene) for gene in gene_list ]
    return list(total_gene_list)

def update_process_list(disease,temp_process_list,gene,disease_process_gene_dict):
    gene_list = [gene]
    process_list = get_connected_processes_of_genes_offline(disease,gene_list,disease_process_gene_dict)
    temp_process_list = set(temp_process_list) - set(process_list)

    return list(temp_process_list)

def main_gene_prior(period):
    print("Performing gene prioritization")
    with open("C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\gene_prioritization\\"+period+"_gene_prioritization_list.txt","w") as gene_prior_file:
        gene_prior_file.write("Disease\tNumber\ttotal set genes\tmin set Genes\n")
        disgenet_list = export_disgenet_neo4j()
        print("length of disease list:",len(disgenet_list))

        disease_process_gene_dict = {}

        for disease in disgenet_list:
            disease=disease['name']
#             print("Disease:",disease)
            disease_process_gene_dict[disease] = {}

            # Get process list of disease from Neo4j
            process_list = get_connected_processes_of_disease_neo4j(disease)

            # Get protein list per process
            disease_process_gene_dict = get_connected_proteins_of_process_neo4j(disease,disease_process_gene_dict,process_list)

            # Get total gene list
            total_gene_list = create_gene_list(disease, process_list,disease_process_gene_dict)
            totat_gene_list_all = total_gene_list
            temp_process_list = list(process_list)

            prior_gene_set = set()
            while len(temp_process_list) != 0:
                # Get number of connected process to each gene
                gene_process_number_dict = get_number_connected_processes_offline(disease,disease_process_gene_dict,total_gene_list)

                # Sorted list of number processes
                sorted_gene_number_process = sorted(gene_process_number_dict.items(), key=lambda kv: kv[1],reverse=True)

                # Add number 1 gene to prior_gene_list
                prior_gene = sorted_gene_number_process[0][0]
                prior_gene_set.add(prior_gene)

                # Update temporary process list
                temp_process_list = update_process_list(disease,temp_process_list, prior_gene,disease_process_gene_dict)

                # Get new gene list
                total_gene_list = create_gene_list(disease, temp_process_list,disease_process_gene_dict)

            total_process_list = get_connected_processes_of_protein_neo4j(totat_gene_list_all)


            gene_prior_file.write(disease+"\t"+str(len(totat_gene_list_all))+"\t"+str(len(prior_gene_set))+"\t"+"|".join(total_process_list)+"\t"+"\t".join(prior_gene_set)+"\n")
