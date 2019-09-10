import time
start = time.time()

tot = 0
for i in range(1,100):
  for j in range(1,100):
    lol = i**j
    if len(str(lol)) == j:
      tot +=1
print(tot)
print(time.time()-start)