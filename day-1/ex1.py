import statistics

size = input('')
numbers = input('')

nbs = sorted([int(n) for n in numbers.split(' ')])

pivot = int(len(nbs) // 2)    
print(int(statistics.median(nbs[:pivot])))
print(int(statistics.median(nbs)))
print(int(statistics.median(nbs[pivot+(0 if (len(nbs) % 2 == 0) else 1):])))   
