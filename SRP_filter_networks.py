from indra.tools import assemble_corpus

# comment out what is needed
network = "Birth"
# network = "Early_gestational_period"
# network = "Infant"
# network = "Late_gestational_period"
# network = "Mid_gestational_period"
# network = "Newborn"


def filter_network(network):
    # Load INDRA statements from pickle file
    pickle = "stmts_3A_original_review_update_network_" + network
    stmts_list = assemble_corpus.load_statements(pickle)

    # INDRA list
    indra_list = []
    for stmt in stmts_list:
        temp_indra_list = []
        indra_gene1 = str(stmt).split(',')[0].split('(')[1]
        indra_gene2 = str(stmt).split(',')[1].split('(')[0].strip()
        temp_indra_list = [indra_gene1, indra_gene2]
        indra_list.append(temp_indra_list)

    # non-overlap list from Genemania
    nonoverlap_list = []
    with open(network + "_non_overlap_excel.txt", "r") as nonoverlap_file:
        for line in nonoverlap_file:
            line = line.rstrip()
            temp_overlap_list = []
            gene1, gene2 = line.split('\t')[0], line.split('\t')[1]
            temp_overlap_list = [gene1, gene2]
            nonoverlap_list.append(temp_overlap_list)

    # removing non-overlapping edges from INDRA list
    denoised_set = set()
    noise_set = set()
    count = 0
    for stmt in stmts_list:
        count += 1
        temp_indra_list = []
        indra_gene1 = str(stmt).split(',')[0].split('(')[1]
        indra_gene2 = str(stmt).split(',')[1].split('(')[0].strip()
        temp_indra_list = [indra_gene1, indra_gene2]
        for x in nonoverlap_list:
            if sorted(temp_indra_list) == sorted(x):
                noise_set.add(stmt)
            if not sorted(temp_indra_list) == sorted(x):
                denoised_set.add(stmt)

    denoised_set = denoised_set - noise_set
    print("Count:", count)
    print("Denoised set:", len(denoised_set))
    print("Noise set:", len(noise_set))

    # Save statements to picklefile


assemble_corpus.dump_statements(denoised_set, network + "_denoised_pickle")
assemble_corpus.dump_statements(noise_set, network + "_noise_pickle")