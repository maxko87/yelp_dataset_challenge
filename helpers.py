
# finds the correlation between two vectors in [-1, 1].
def correlation(X, Y):
    if len(X) != len(Y):
        raise Exception("Two vectors must be the same length.")
    nX = 1/(sum([x*x for x in X]) ** 0.5)
    nY = 1/(sum([y*y for y in Y]) ** 0.5)
    cor = sum([(x*nX)*(y*nY)  for x,y in zip(X,Y) ])
    return cor