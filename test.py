'''
A matrix of full connectivity of businesses where
the edge weights are the distance between two businesses
'''

import load_data
import math, numpy as np
#1 degree of latitude is approx 69 miles
n = 5
businesses = load_data.load_objects("business", n)
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
  print i
  A.append(dists)
print max(A[1])
#makes the matrix row stochastic (rows sum to 1)
for i in range(n):
  s = sum(A[i])
  A[i][0:] = [x/s for x in A[i][0:]]
print A
b = [0]*n
b[1] = 1
print b
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
print eigenvectors