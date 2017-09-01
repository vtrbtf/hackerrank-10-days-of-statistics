from math import factorial
p = 12 / 100
batch_size = 10

def binomial_distribution(x,n,p):
    return (factorial(n) / (factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))

print("%.3f" % sum(list(map(lambda x: binomial_distribution(x, batch_size, p),  range(0,3)))))
print("%.3f" % sum(list(map(lambda x: binomial_distribution(x, batch_size, p),  range(2,11)))))
