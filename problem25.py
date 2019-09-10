import time
start = time.time()

fibs = [0, 1]
for i in range(2, 10000000+1):
  fibs.append(fibs[-1] + fibs[-2])
  if fibs[-1] > (10**999):
    break
print(len(fibs)-1)
print(time.time()-start)

#not quite sure how this worked