'''
Determines if a review is fake (specifically, calculates a fakeness coefficient)
Criteria for a fake review:
    - user has low degree centrality (has rated few businesses)
    - business has low degree centrality (has been rated by few users)
    - user is unusually enthusiastic
'''

from objects import *
from networkx import *
from helpers import *
import load_data, idea_1, idea_6
import re


def get_fake_coeff(review):
    G = idea_1.get_bipartite_graph()


