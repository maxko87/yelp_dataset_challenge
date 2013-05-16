'''
Nodes: businesses
Edges: if a user reviewed b1 followed by b2, create from b1 to b2,
    weighted by number of occurences
'''

from objects import *
from networkx import *
from helpers import *
import load_data
import re, datetime
from dateutil import parser

def get_temporal_business_graph():

    businesses = load_data.load_objects("business")
    users = load_data.load_objects("user")
    reviews = load_data.load_objects("review", 10000)

    business_dict = {}
    for b in businesses:
        business_dict[b.business_id] = b
    user_dict = {}
    for u in users:
        user_dict[u.user_id] = u
    # create dictionary of user_id -> [review, ...]
    review_dict = {}
    for review in reviews:
        if 'Restaurants' not in business_dict[review.business_id].categories:
            continue
        if review.user_id in review_dict.keys():
            review_dict[review.user_id] += [review]
        else:
            review_dict[review.user_id] = [review]

    G = nx.DiGraph()

    for user_id, review_list in review_dict.items():
        review_list = sorted(review_list, key=lambda review: review.date)
        for i in range(len(review_list) - 1):
            
            d1 = parser.parse(review_list[i].date)
            d2 = parser.parse(review_list[i+1].date)
            b1 = business_dict[review_list[i].business_id]
            b2 = business_dict[review_list[i+1].business_id]
            if G.has_edge(b1, b2):
                G.edge[b1][b2]['weight'] += 1
            else:
                G.add_edge(b1, b2)
                G.edge[b1][b2]['weight'] = 1
            '''
            b1 = business_dict[review_list[i].business_id]
            b2 = business_dict[review_list[i+1].business_id]
            for c1 in b1.categories:
                for c2 in b2.categories:
                    if G.has_edge(c1, c2):
                        G.edge[c1][c2]['weight'] += 1
                    else:
                        G.add_edge(c1, c2)
                        G.edge[c1][c2]['weight'] = 1
            '''

    print "graph created"
    return G

G = get_temporal_business_graph()

init_weights = {} # for pagerank
for node in G:  
    #init_weights[node] = node.stars #node.stars or node.review_count
    init_weights[node] = 1

# pick a centrality
#centrality = nx.degree_centrality(G)
#centrality = nx.betweenness_centrality(G)
#centrality = nx.closeness_centrality(G, distance=True)    
centrality = nx.eigenvector_centrality(G, tol=.01)  # converges with tol >=.01
#centrality = nx.pagerank(G, personalization=init_weights)

centralities = sorted([(b, centr) for b, centr in centrality.items()], key=lambda tup: tup[1], reverse=True)

for b, centr in centralities[:50]:
    print '{:<70}'.format(str(b)), "\t\t\t", centr, "\t\t\t", b.stars, "\t\t\t", b.review_count
    #print '{:<70}'.format(str(b)), "\t\t\t", centr

ctrs = [centr for (b, centr) in centralities]
stars = [b.stars for (b, centr) in centralities]

print correlation(ctrs, stars)
