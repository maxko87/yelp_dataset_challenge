'''
find underrated businesses - have a low average review, 
    but only because reviewers of that business tended to be harsher critics
'''

from objects import *
from networkx import *
from helpers import *
import load_data
import re

def run():

    businesses = load_data.load_objects("business")
    users = load_data.load_objects("user")
    reviews = load_data.load_objects("review", 100000)

    business_dict = {}
    for b in businesses:
        business_dict[b.business_id] = b
    user_dict = {}
    for u in users:
        user_dict[u.user_id] = u

    # user gave 4.5, usually gives 3
    b_dict = {} # business -> (total_reviewer_plus_or_minus, num_reviews_seen)
    for review in reviews:
        if review.business_id not in business_dict or review.user_id not in user_dict:
            continue
        b = business_dict[review.business_id]
        u = user_dict[review.user_id]
        diff = review.stars - u.average_stars
        if b in b_dict:
            b_dict[b] = (b_dict[b][0] + diff, b_dict[b][1] + 1)
        else:
            b_dict[b] = (diff, 1)

    normalized_businesses = []
    for b in b_dict:
        diff, count = b_dict[b]
        if count > 1:
            new_rating = b.stars + diff
            normalized_businesses += [(b, new_rating, count)]

    normalized_businesses = sorted(normalized_businesses, key=lambda t: t[1], reverse=True)


    print "\n\nunderrated businesses"
    for b, rating, count in normalized_businesses[:20]:
        print '{:<80}'.format(str(b)), "\t\t\t", rating, "\t\t\t", count, "/", b.review_count, "\t\t\t", b.stars

    print "\n\noverrated businesses"
    for b, rating, count in normalized_businesses[-20:]:
        print '{:<80}'.format(str(b)), "\t\t\t", rating, "\t\t\t", count, "/", b.review_count, "\t\t\t", b.stars

run()