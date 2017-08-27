import statistics

size = input('')
numbers = input('')
freq = input('')


nbs = [int(n) for n in numbers.split(' ')]
fq = [int(n) for n in freq.split(' ')]

nbs = sorted([item for id, n in enumerate(nbs) for item in (fq[id] * [n])])

pivot = int(len(nbs) // 2)
q3 = statistics.median(nbs[pivot+(0 if (len(nbs) % 2 == 0) else 1):])    
q1 = statistics.median(nbs[:pivot])
print("%.1f" %  (q3 - q1))   