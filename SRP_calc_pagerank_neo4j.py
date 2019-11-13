def get_pagerank():
    g = connect_to_graph()
    pagerank_dict = {}
    pagerank_dict['Disease'] = {}
    pagerank_dict['GO'] = {}
    pagerank_dict['bioprocess'] = {}
    pagerank_dict['protein'] = {}
    pagerank_dict['gene'] = {}
    pagerank_dict['chemical'] = {}
    pagerank_dict['proteinfamily'] = {}
    pagerank_dict['other'] = {}

    pagerank_result = g.run(
        "CALL algo.pageRank.stream('', '', {iterations:20, dampingFactor:0.85}) YIELD nodeId, score RETURN algo.asNode(nodeId).name AS name, labels(algo.asNode(nodeId)) AS label ,score ORDER BY score DESC")
    pagerank_data = pagerank_result.data()
    for x in pagerank_data:
        name = x['name']
        label = x['label']
        if label == ['Disease']:
            pagerank_dict['Disease'][name] = x['score']
        if label == ['GO', 'GOslim'] or label == ['GO'] or label == ['GOslim']:
            pagerank_dict['GO'][name] = x['score']
        if label == ['INDRA', 'bioprocess']:
            pagerank_dict['bioprocess'][name] = x['score']
        if label == ['INDRA', 'protein']:
            pagerank_dict['protein'][name] = x['score']
        if label == ['gene'] or label == ['INDRA', 'protein', 'gene']:
            pagerank_dict['gene'][name] = x['score']
        if label == ['INDRA', 'chemical']:
            pagerank_dict['chemical'][name] = x['score']
        if label == ['INDRA', 'proteinfamily']:
            pagerank_dict['proteinfamily'][name] = x['score']
        if label == ['INDRA', 'other']:
            pagerank_dict['other'][name] = x['score']
    sorted_disease_pagerank = sorted(pagerank_dict['Disease'].items(), key=lambda kv: kv[1], reverse=True)

    return pagerank_dict


pagerank_dict = get_pagerank()
with open("C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\neo4j\\pagerank\\Pagerank_3B.txt", "w") as pagerankfile:
    for x in pagerank_dict:

        for y in pagerank_dict[x]:
            pagerankfile.write(x + '\t')
            pagerankfile.write(y + '\t')
            pagerankfile.write(str(pagerank_dict[x][y]) + '\n')
get_pagerank()