import time
start = time.time()

eight = 0
temp = []
good = []

for i in range(2,10000000):
  k = i
  if i % 1000 == 0:
    print(eight)
  while k != 89:
    if k not in good:
      temp.append(k)
      if k == 1:
        temp = []
        break
      else:
        k = sum([int(j)**2 for j in str(k)]) 
    else:
      eight+=1
      good.append(temp)
      temp = []
      break
  else:
    eight+=1
print(eight)

print(time.time()-start)