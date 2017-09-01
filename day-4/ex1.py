from math import factorial
ratio_A = 1.09
ratio_B = 1
p = ratio_A / (ratio_A + ratio_B)

def binomial_distribution(x,n,p):
    return (factorial(n) / (factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))

print("%.3f" % sum(list(map(lambda x: binomial_distribution(x, 6, p),  range(3,7)))))
