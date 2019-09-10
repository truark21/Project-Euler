import time
start = time.time()

from itertools import permutations
alist = [0,1,2,3,4,5,6,7,8,9]
perm = permutations(alist)
print(list(perm)[1000000-1])


end = time.time()
print(end-start)