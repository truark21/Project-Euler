import time
start = time.time()

lol = 0
for i in range(100,1,-1):
  for j in range(100,1,-1):
    blah = i**j
    blah = sum([int(k) for k in str(blah)])
    if lol < blah:
      lol = blah
print(lol)
  
print(time.time()-start)