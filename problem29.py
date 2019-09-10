import time
start = time.time()

lol = []

for i in range(2,101):
  for j in range(2,101):
    if i**j not in lol:
      lol.append(i**j)
print(len(lol))
print(time.time()-start)

#RUNS MUCH FASTER SINCE YOU DONT CHECK AND JUST TURN INTO A SET WHICH HAS NO DUPS
import time
start = time.time()

lol = []

for i in range(2,101):
  for j in range(2,101):
    lol.append(i**j)
lol = list(set(lol))
print(len(lol))
print(time.time()-start)