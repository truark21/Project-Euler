import time
start = time.time()
y = []
x = []
k=1
tots = 0

while k<10000:
  for i in range(1,k/2+1):#sub 220 for k and check with thing below second loop
    if k%i == 0:
      y.append(i)
  for j in range(1,sum(y)/2+1):
    if sum(y)%j == 0:
      x.append(j)
  if k == sum(x) and sum(x) != sum(y):
    tots += sum(x)
    tots += sum(y)
    print(sum(x),sum(y))
  y = []
  x = []
  k+=1

print(tots/2)
print(time.time()-start)