'''
Create a bipartite graphs of words in review text to reviews that contain them.
'''

from objects import *
from networkx import *
from helpers import *
import load_data
import re

reviews = load_data.load_objects("review", 1000)

G = nx.Graph()

init_weights = {}
for review in reviews:
    for word in re.split(" |\. |\! ", review.text):
        word = word.lower()
        G.add_edge(word, review)
        G.edge[word][review]['weight'] = review.stars
        #init_weights[review] = review.stars
        #init_weights[word] = 1

# pick a centrality
#centrality = nx.degree_centrality(G)     
#centrality = nx.betweenness_centrality(G)
#centrality = nx.closeness_centrality(G, distance=True)    
#centrality = nx.eigenvector_centrality(G, tol=.01)
#centrality = nx.pagerank(G, personalization=init_weights) 

just_words = {}
for word, freq in centrality.iteritems():
    if type(word) != Review:
        just_words[word] = freq
centrality = just_words

centralities = [(word, freq) for word, freq in centrality.iteritems()]

centralities = sorted(centralities, key=lambda tuple: tuple[1], reverse=True)
for word, freq in centralities[:50]:
    print word, freq