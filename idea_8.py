'''
Cluster businesses by category and examine outdegree to other categories
to figure out which businesses types are the most (e.g. if users rate these
categories, they are unlikely to rate others) 
'''
from collections import defaultdict
from objects import *
from networkx import *
from helpers import *
import load_data, idea_4

'''
categories = []
businesses = load_data.load_objects("business")
for b in businesses:
    for c in b.categories:
        if c not in categories and 'Restaurants' in b.categories:
            categories += [c]
print categories
'''
categories = [u'Food', u'Bagels', u'Delis', u'Restaurants', u'Sandwiches', u'Mexican', u'Pizza', u'Burgers', u'Buffets', u'Dim Sum', u'Chinese', u'Fast Food', u'Breweries', u'American (New)', u'Caterers', u'Event Planning & Services', u'Italian', u'Cheesesteaks', u'Pubs', u'Bars', u'Nightlife', u'British', u'Arts & Entertainment', u'Arcades', u'Japanese', u'Bakeries', u'American (Traditional)', u'Dive Bars', u'Hot Dogs', u'Breakfast & Brunch', u'Diners', u'Sushi Bars', u'Tex-Mex', u'Mediterranean', u'Beer, Wine & Spirits', u'Gay Bars', u'Fish & Chips', u'Coffee & Tea', u'Dry Cleaning & Laundry', u'Local Services', u'Convenience Stores', u'Korean', u'Sports Bars', u'Comfort Food', u'Seafood', u'Cajun/Creole', u'Vegan', u'Health Markets', u'Specialty Food', u'Greek', u'Ice Cream & Frozen Yogurt', u'Caribbean', u'Vegetarian', u'Barbeque', u'Food Delivery Services', u'Middle Eastern', u'Taiwanese', u'Cafes', u'Wine Bars', u'French', u'Latin American', u'Asian Fusion', u'Food Stands', u'Indian', u'Pakistani', u'Persian/Iranian', u'Thai', u'Hawaiian', u'Juice Bars & Smoothies', u'Filipino', u'Ethiopian', u'Vietnamese', u'Basque', u'Spanish', u'Steakhouses', u'Kosher', u'Lounges', u'Music Venues', u'Cinema', u'Southern', u'Chicken Wings', u'Donuts', u'Irish', u'Grocery', u'Gluten-Free', u'Soul Food', u'German', u'Hotels & Travel', u'Hotels', u'Halal', u'Active Life', u'Stadiums & Arenas', u'Horse Racing', u'African', u'Creperies', u'Cuban', u'Landmarks & Historical Buildings', u'Public Services & Government', u'Desserts', u'Dance Clubs', u'Ethnic Food', u'Jazz & Blues', u'Gastropubs', u'Mongolian', u'Street Vendors', u'Venues & Event Spaces', u'Do-It-Yourself Food', u'Soup', u'Turkish', u'Tapas Bars', u'Golf', u'Seafood Markets', u'Fondue', u'Karaoke', u'Food Trucks', u'Gelato', u'Tennis', u'Gyms', u'Fitness & Instruction', u'Salad', u'Polish', u'Live/Raw Food', u'Pool Halls', u'Local Flavor', u'Cambodian', u'Tapas/Small Plates', u'Peruvian', u'Tea Rooms', u'Cheese Shops', u'Scandinavian', u'Health & Medical', u'Hospitals', u'Russian', u'Shopping Centers', u'Shopping', u'Outlet Stores', u'Piano Bars', u'Colleges & Universities', u'Education', u'Wedding Planning', u'Fruits & Veggies', u'Chocolatiers & Shops', u'Afghan', u'Modern European', u'Sporting Goods', u'Party & Event Planning', u'Brazilian', u'Amusement Parks', u'Burmese', u'Day Spas', u'Beauty & Spas', u'Meat Shops', u'Argentine', u'Laotian', u'Lebanese', u'Florists', u'Flowers & Gifts', u'Tours', u'Automotive']

G = idea_4.get_graph(NUM_REVIEWS=20000)

'''
chinese:
    chinese: 500
    korean: 300
    mexican: 100
korean:
    ...
'''

d = defaultdict(dict)
for c1 in categories:
    for c2 in categories:
        if c1 != 'Restaurants' and c2 != 'Restaurants':
            d[c1][c2] = 0

for b1, b2 in G.edges():
    same_category = False
    for c1 in b1.categories:
        for c2 in b2.categories:
            if c1 == c2 and c1 != 'Restaurants':
                d[c1][c2] += 1
                same_category = True
    # count restaurants as the same category if they share any category
    if not same_category:
        for c1 in b1.categories:
            for c2 in b2.categories:
                if c1 != 'Restaurants' and c2 != 'Restaurants':
                    d[c1][c2] += 1
                    d[c2][c1] += 1

# store list of (category, internal edges, external edges)
homophily = []
for c1 in d:
    external, internal = 0, 0
    for c2 in d[c1]:
        if c1 == c2:
            internal = d[c1][c2]
        else:
            external += d[c1][c2]
    homophily += [(c1, internal, external)]

def sort_helper(t):
    try:
        if t[1] > 0:
            return float(t[1])/t[2]
        else:
            return -t[2]
    except:
        return 0

homophily = sorted(homophily, key = lambda t: sort_helper(t), reverse=True)

print "\n\nhighest homophily: "
for category, internal, external in homophily[:30]:
    print category, internal, external

print "\n\nlowest homophily: "
for category, internal, external in homophily[-30:]:
    print category, internal, external


