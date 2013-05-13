'''
A matrix of full connectivity of businesses where
the edge weights are the distance between two businesses
'''

import load_data
import math, numpy as np
from helpers import *

#1 degree of latitude is approx 69 miles
n = 500
pre_businesses = load_data.load_objects("business", n)

businesses=[]
for b in pre_businesses:
  if 'Restaurants' in b.categories:
    businesses += [b]

n = len(businesses)
for b in businesses:
  print "rating for ",str(b), ":", b.stars, ", # reviews: ", b.review_count

#users = load_data.load_objects("user", 5000)
#reviews = load_data.load_objects("review", 50000)
A = []
print 'starting script'
for i in range(n):
  bus = businesses[i]
  dists = []
  for j in range(n):
    if (i==j):
      dists.append(0)
      continue
    bus2 = businesses[j]
    lat_dist = bus.latitude-bus2.latitude
    long_dist = bus.longitude-bus2.longitude
    latlongdist = math.sqrt(math.pow(lat_dist,2) + math.pow(long_dist,2))
    dists.append(1/latlongdist)
  A.append(dists)
#makes the matrix row stochastic (rows sum to 1)
#for i in range(n):
  #s = sum(A[i])
  #A[i][0:] = [x/s for x in A[i][0:]]
#b = A*b
'''
for x in range(10):
  for i in range(n):
    #not sure if this is correct to do A*b
    b[i] = sum([A[i][j]*b[j] for j in range(n)])
print b
'''

eigenvalues, eigenvectors = np.linalg.eig(A)
print eigenvalues
rankings  = []
for row in eigenvectors:
  rankings += [row[0]]

stars_cor = []
review_count_corr = []

for i in range(len(businesses)):
  stars_cor += [businesses[i].stars]
  review_count_corr += [businesses[i].review_count]


print ("stars correlation: " + str(correlation(rankings, stars_cor)))
print ("review count correlation: " + str(correlation(rankings, review_count_corr)))
