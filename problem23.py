import time
from math import sqrt
start = time.time()

def perfect(n):
  step = 2 if n%2 else 1
  return set(reduce(list.__add__,([i,n//i] for i in range(1,int(sqrt(n))+1,step) if n%i==0)))

def prime(n):
  h = [True] * (n+1)
  p = 2
  while(p*p <= n):
    if(h[p] == True):#checks to see if that value is good
      for i in range(p*2,n+1,p):#loops through the multiples and makes them false
        h[i] = False
    p+=1
    

#prime(40)#prints all primes under 40
#print(perfect(30))
#print(sorted([perfect(26)]))

yes = []
k = set()
ha = 0
for i in range(1,28123):
  if not prime(i):
    b = list(perfect(i))
    b.remove(max(perfect(i)))
    if sum(b) > i:
      yes.append(i)
for i in range(len(yes)):
  for j in range(i,len(yes)):
    if (yes[i]+yes[j]) < 28123:
      k.add(yes[i]+yes[j])
    else:
      break
for i in range(1,28123):
  if i not in k:
    ha+=i
print(ha)
print(time.time()-start)