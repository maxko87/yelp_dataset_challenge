'''
Another graph that we could look at would be one where businesses are nodes, and edges are present 
if a user has rated both of the businesses.  Classifying the nodes according to other data we have 
(like their category), we could use metrics of the graph to determine if we can draw conclusions 
on either a businesses' popularity (star rating), or the actions of users (do users typically like 
to rate only businesses of a certain type, or are relationships such as: "Users who rate two Chinese 
restaurants are also likely to rate a Mexican restaurant" that we can determine from the data.)

graph businesses as nodes, edges based on num users rating both of those businesses
    - calculate some sort of similarity metric between businesses
    - e.g. high weight edges expected between nodes that are either close in location, same type of food, etc.
        - what if neither of those explain the similarity fully? we look at review texts to find out why
'''
from objects import *
from networkx import *
from helpers import *
import load_data

businesses = load_data.load_objects("business")
business_dict = {}
for b in businesses:
    business_dict[b.business_id] = b
reviews = load_data.load_objects("review", 20000)

# first, create a mapping of user -> [businesses rated]
# second, create a mapping of (b1, b2) -> number of users rating both 
first = {}
for index, review in enumerate(reviews):
    if index%1000 == 0:
        print index
    if review.user_id in first.keys():
        first[review.user_id] += [review.business_id]
    else:
        first[review.user_id] = [review.business_id]

print "number of users: " + str(len(first))

second = {}
for user_id in first.keys():
    for b1 in first[user_id]:
        for b2 in first[user_id]:
            if b1 != b2:
                # for b1=123, b2=524, we use key = 123_AND_524
                key = [b1, b2]
                sorted(key)
                key = '_AND_'.join(key)
                if set(key) in second.keys():
                    second[key] += 1
                else:
                    second[key] = 1

print "number of business pairs: " +  str(len(second))

G = nx.Graph()

for key in second.keys():
    if second[key] > 1:
        print key
    b1_id, b2_id = key.split("_AND_")
    G.add_edge(business_dict[b1_id], business_dict[b2_id])


