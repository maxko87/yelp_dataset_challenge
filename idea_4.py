'''
Another graph that we could look at would be one where businesses are nodes, and edges are present 
if a user has rated both of the businesses.  Classifying the nodes according to other data we have 
(like their category), we could use metrics of the graph to determine if we can draw conclusions 
on either a businesses’ popularity (star rating), or the actions of users (do users typically like 
to rate only businesses of a certain type, or are relationships such as: “Users who rate two Chinese 
restaurants are also likely to rate a Mexican restaurant” that we can determine from the data.)

graph businesses as nodes, edges based on num users rating both of those businesses
    - calculate some sort of similarity metric between businesses
    - e.g. high weight edges expected between nodes that are either close in location, same type of food, etc.
        - what if neither of those explain the similarity fully? we look at review texts to find out why
'''

import load_data

businesses = load_data.load_objects("business", 1000)
users = load_data.load_objects("user", 5000)
reviews = load_data.load_objects("review", 6000)

# maps nodes to a list of nodes they are connected to
graph = {}
for user in users:
    if 
