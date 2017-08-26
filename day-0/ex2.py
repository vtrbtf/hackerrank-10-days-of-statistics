import statistics

size = input('')
numbers = input('')
weights = input('')

nbs = [int(n) for n in numbers.split(' ')]
wgts = [int(n) for n in weights.split(' ')]

print("%.1f" % (sum([wgts[i] * n for i,n in enumerate(nbs)])/sum(wgts)))
