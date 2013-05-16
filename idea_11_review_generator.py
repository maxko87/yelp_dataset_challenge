'''
generate reviews for a given 
'''

from objects import *
from networkx import *
from helpers import *
import load_data
import re, random, unicodedata

NUM_STATES = 2 # number of previous words to use as state
NUM_REVIEWS = 100000
PUNCTUATION = ['.', '!', '?']

businesses = load_data.load_objects("business")
users = load_data.load_objects("user")
reviews = load_data.load_objects("review", NUM_REVIEWS)
print NUM_REVIEWS,"reviews loaded"

business_dict = {}
for b in businesses:
    business_dict[b.business_id] = b
user_dict = {}
for u in users:
    user_dict[u.user_id] = u

# creates a text file with the appropriate reviews:
def make_reviews_file(stars=None, min_stars=None, max_stars=None, category=None):
    F_NAME = 'reviews_file'
    f = open(F_NAME, 'w')
    num_reviews = 0
    for review in reviews:
        # check all criteria for reviews
        if 'Restaurants' in business_dict[review.business_id].categories and \
                (not stars or stars == review.stars) and \
                (not min_stars or review.stars >= min_stars) and \
                (not max_stars or review.stars >= min_stars) and \
                (not category or category in business_dict[review.business_id].categories): 
            text = unicodedata.normalize('NFKD', review.text).encode('ascii','ignore')
            f.write(text)
            num_reviews += 1
    print "made reviews file with", num_reviews, "reviews"
    return F_NAME

# generates markov chain from reviews in a file
def get_markov_chain(text_file):

    starting_table = {} # beginnings of sentences
    table = {} # anywhere in a sentence
    fallback_table = {} # only bases on previous word

    with open(text_file, 'r') as f:
        for review in f.readlines():
            words = review.split()
            for i in range(len(words)-NUM_STATES-1):
                # check whether is start of sentence
                if i==0 or words[i-1][-1] in PUNCTUATION:
                    d = starting_table
                else:
                    d = table
                # build the key
                key = []
                for j in range(NUM_STATES):
                    key += [words[i+j].lower()]
                key = tuple(key)
                # add the predicted word
                if key in d:
                    d[key] += [words[i+NUM_STATES+1].lower()]
                else:
                    d[key] = [words[i+NUM_STATES+1].lower()]
                # add to fallback table
                if i > 0:
                    key = words[i-1].lower()
                    if key in fallback_table:
                        fallback_table[key] += [words[i].lower()]
                    else:
                        fallback_table[key] = [words[i].lower()]

    print "created markov chain tables"
    return (starting_table, table, fallback_table)

def generate_review(words, stars=None,min_stars=None, max_stars=None, category=None):
    f_name = make_reviews_file(stars, min_stars, max_stars, category)
    starting_table, table, fallback_table = get_markov_chain(f_name)

    review = []
    fallbacks, successes = 0, 0
    for i in range(words):
        # new sentence
        if i==0 or review[i-1][-1] in PUNCTUATION:
            k = starting_table.keys()
            sentence_start_words = k[int(random.random()*len(k))]
            for w in sentence_start_words:
                review += [w]
        # continue sentence
        else:
            key = []
            for j in range(NUM_STATES):
                key += [review[i-NUM_STATES+j]]
            key = tuple(key)
            if key in table:
                choices_for_next_word = table[key]
                successes += 1
            elif review[i-1] in fallback_table: # fall back to one word chain 
                choices_for_next_word = fallback_table[review[i-1]]
                fallbacks += 1
            else: # major fail
                choices_for_next_word = ['and', 'or']
                fallbacks += 1
            word = choices_for_next_word[int(random.random()*len(choices_for_next_word))]
            review += [word]
            
    print "fallbacks:", fallbacks, "successes:", successes
    return ' '.join(review)


#print "500 words, any stars, any category: " + generate_review(500) + "\n\n"
#print "500 words, 4+ stars, any category: " + generate_review(500, min_stars=4) + "\n\n"
#print "500 words, 2- stars, any category: " + generate_review(500, max_stars=2) + "\n\n"
#print "500 words, 4+ stars, Chinese: " + generate_review(500, min_stars=3, category='Chinese') + "\n\n"
#print "500 words, 2- stars, Mexican: " + generate_review(500, max_stars=3, category='Mexican') + "\n\n"
#print "500 words, Chinese: " + generate_review(500, category='Chinese') + "\n\n"
print "500 words, Bars: " + generate_review(500, category='Bars') + "\n\n"

