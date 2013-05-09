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

import load_data

#businesses = load_data.load_objects("business", 1000)
#users = load_data.load_objects("user", 5000)
reviews = load_data.load_objects("review", 50000)

# first, create a mapping of user -> [businesses rated]
# second, create a mapping of (b1, b2) -> number of users rating both 
first = {}
for review in reviews:
    if review.user_id in first.keys():
        first[review.user_id] += [review.business_id]
    else:
        first[review.user_id] = [review.business_id]

#print "first: " + str(first)

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

print len(second)
for key in second.keys():
    if second[key] > 1:
        print key, second[key]

