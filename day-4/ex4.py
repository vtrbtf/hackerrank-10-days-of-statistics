p = 1 / 3

def g(n,p):
    return ((1 - p) ** (n - 1)) * p

print("%.3f" % sum(list(map(lambda x: g(x, p), range(1,6)))))

