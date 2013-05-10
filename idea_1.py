'''
Construct a bipartite graph with users and businesses as the nodes. 
When a user rates a business, a link is created.  Edges can be weighted 
with different metrics, such as the star rating, or the number of useful
votes the review got.  We could then compute different centrality measures 
for the businesses and analyze them to determine how they may relate to a 
businesses' popularity.
'''

import load_data, cPickle as pickle, time, pprint
from objects import *
from networkx import *
from helpers import *
pp = pprint.PrettyPrinter(indent=4)
start = time.clock()

NUM_REVIEWS = 500 # limiting factor for speed of the code. only up to 1000 will run reasonably fast


businesses = load_data.load_objects("business")
print "businesses loaded: " + str(time.clock() - start)
users = load_data.load_objects("user")
print "users loaded: " + str(time.clock() - start)
reviews = load_data.load_objects("review", NUM_REVIEWS)
print "reviews loaded: " + str(time.clock() - start)

business_dict = {}
for b in businesses:
    business_dict[b.business_id] = b
user_dict = {}
for u in users:
    user_dict[u.user_id] = u

print "dicts loaded: " + str(time.clock() - start)

G = nx.Graph()

for r in reviews:
    if r.user_id in user_dict.keys() and b.business_id in business_dict.keys():
        user = user_dict[r.user_id]
        business = business_dict[r.business_id]
        G.add_edge(user, business)
        G.edge[user][business]['weight'] = r.stars # r.stars or r.votes[funny, useful, cool]

print "graph fully loaded: " + str(time.clock() - start)

# pick your poison
centrality = nx.degree_centrality(G)       # n(500)=0.93
#centrality = nx.betweenness_centrality(G)  # n(500)=0.76
#centrality = nx.closeness_centrality(G)    # n(500)=0.92
#centrality = nx.eigenvector_centrality(G)  # n(500)=0.92

print "centralities calculated: " + str(time.clock() - start)

pp.pprint(centrality)

# store the business name and two metric we wish to find the correlation between
businesses = []
ratings = []
centralities = []

for b_or_u in centrality.keys():
    if type(b_or_u) == Business and centrality[b_or_u] > 0:
        b = b_or_u
        businesses += [b.name]
        ratings += [b.stars]
        centralities += [centrality[b]]

print "nonzero centralities saved: " + str(time.clock() - start)

print "CORRELATION: " + str(correlation(ratings, centralities))









