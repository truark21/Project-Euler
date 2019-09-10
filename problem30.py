import time
start = time.time()

lol = 0
for i in range(100,1000000):
  tot = 0
  blah = list(str(i))
  for j in range(len(blah)):
    tot += int(blah[j])**5
  if tot == i:
    lol +=tot
print(lol)
print(time.time()-start)