'''
Bipartite graph of words to supernodes of star ratings of review that
contain those words, with edge weights of the number of occurences.
We try to find if any words are particularly telling of a star rating.
'''

from objects import *
from networkx import *
from helpers import *
import load_data
import re

def run():

    businesses = load_data.load_objects("business")
    business_dict = {}
    for b in businesses:
        business_dict[b.business_id] = b
    reviews = load_data.load_objects("review", 25000)

    G = nx.DiGraph()

    for review in reviews:
        b = business_dict[review.business_id]
        if 'Restaurants' not in b.categories:
            continue
        text = re.sub('[^a-zA-Z0-9\n]', ' ', review.text)
        words_used = []
        for word in re.split(" ", text):
            word = word.lower()
            if word in words_used: # only count one word occurence per review
                continue
            words_used += [word]
            if (review.stars not in G):
                G.add_node(review.stars)
            if (word not in G):
                G.add_node(word)
            if not G.has_edge(word, review.stars):
                G.add_edge(word, review.stars)
                G.edge[word][review.stars]['weight'] = 1
            else:
                G.edge[word][review.stars]['weight'] += 1

    indicators = []
    for word in G:
        if G.out_degree(word) > 0: # is a word
            max_stars, max_weight = 0, 0
            # find which rating this word is most indicative of
            for stars in G.neighbors(word):
                if G.edge[word][stars]['weight'] > max_weight:
                    max_stars = stars
                    max_weight = G.edge[word][stars]['weight']
            # find how indicative this word is of that rating (and ratings nearby)
            indicator = max_weight
            for stars in G.neighbors(word):
                indicator -= abs(stars - max_stars) * G.edge[word][stars]['weight']
            indicators += [(word, indicator, max_stars)]

    # sort by best indicators
    indicators = sorted(indicators, key = lambda tuple: tuple[1], reverse=True)

    return indicators

indicators = run()

i=0
for word, indicator, max_stars in indicators[:50]:
    #if max_stars < 3:
        #i += 1
    print word, indicator, max_stars
    if i == 50:
        break