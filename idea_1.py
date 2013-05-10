'''
Construct a bipartite graph with users and businesses as the nodes. 
When a user rates a business, a link is created.  Edges can be weighted 
with different metrics, such as the star rating, or the number of useful
votes the review got.  We could then compute different centrality measures 
for the businesses and analyze them to determine how they may relate to a 
businesses' popularity.
'''

import load_data, cPickle as pickle, time, pprint
from networkx import *
pp = pprint.PrettyPrinter(indent=4)
start = time.clock()

businesses = load_data.load_objects("business")
print "businesses loaded: " + str(time.clock() - start)
users = load_data.load_objects("user")
print "users loaded: " + str(time.clock() - start)
reviews = load_data.load_objects("review", 1000)
print "reviews loaded: " + str(time.clock() - start)

business_dict = {}
for b in businesses:
    business_dict[b.business_id] = b
user_dict = {}
for u in users:
    user_dict[u.user_id] = u

print "dicts loaded: " + str(time.clock() - start)


G = nx.Graph()

'''
for b in business_dict.values():
    G.add_node(b)
for u in user_dict.values():
    G.add_node(u)
print "all nodes added: " + str(time.clock() - start)
'''

for r in reviews:
    if r.user_id in user_dict.keys() and b.business_id in business_dict.keys():
        user = user_dict[r.user_id]
        business = business_dict[r.business_id]
        G.add_edge(user, business)
        G.edge[user][business]['weight'] = r.stars

print "graph fully loaded: " + str(time.clock() - start)

pp.pprint( nx.betweenness_centrality(G) )



# first, create a mapping of user -> [businesses rated]
# second, create a mapping of (b1, b2) -> number of users rating both 

