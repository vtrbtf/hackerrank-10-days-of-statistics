import statistics
import math
size = input('')
numbers = input('')
nbs = [int(n) for n in numbers.split(' ')]
m = statistics.mean(nbs)
print("%.1f" % math.sqrt(sum([(n - m) ** 2 for n in nbs]) / len(nbs)))