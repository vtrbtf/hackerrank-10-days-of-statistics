from math import factorial
X = 5
mean = 2.5
e = 2.71828

def poisson_dist(X, mean):
    return ((mean ** X) * (e ** (-1 * mean))) / factorial(X)

print("%.3f" % poisson_dist(X, mean))
