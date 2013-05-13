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

NUM_REVIEWS = 1500 # limiting factor for speed of the code. only up to 1000 will run reasonably fast


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

#G = nx.DiGraph()
G = nx.Graph()

for index, r in enumerate(reviews):
    if (index % 100) == 0:
        print index
    if r.user_id in user_dict.keys() and b.business_id in business_dict.keys():
        user = user_dict[r.user_id]
        business = business_dict[r.business_id]
        G.add_edge(business, user)
        G.edge[business][user]['weight'] = r.stars # r.stars or r.votes[funny, useful, cool]

print "graph fully loaded: " + str(time.clock() - start)

init_weights = {} # for pagerank
for node in G:  
    if type(node) == Business:
        init_weights[node] = node.stars #node.stars or node.review_count
    elif type(node) == User:
        init_weights[node] = 1

# pick a centrality
#centrality = nx.degree_centrality(G)       # n(500)=0.93, n(1500)=.86
#centrality = nx.betweenness_centrality(G)  # n(500)=0.76, n(1500)=.32
#centrality = nx.closeness_centrality(G, distance=True)    
    
    # n(500, false)=0.92, n(500, r.stars)=.80
    # n(500, funny)=.65, n(500, useful)=.59, n(500, cool)=.61

    # n(1500, false)=.82, n(1500, r.stars)=.78

centrality = nx.eigenvector_centrality(G, tol=.01)  # converges with tol >=.01
    #n(500)=.83, n(1500)=.75
#centrality = nx.pagerank(G, personalization=init_weights) 
    #n(500, false)=.98, n(500, stars)=.995, n(500, review_count)=.91
    #n(3000, stars)=.994

print "centralities calculated: " + str(time.clock() - start)

#pp.pprint(centrality)

# store the business name and two metrics we wish to find the correlation between
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









