import time
start = time.time()

def prime(n):
  h = [True] * (n+1)
  p = 2
  primes = []
  while(p*p <= n):
    if(h[p] == True):#checks to see if that value is good
      for i in range(p*2,n+1,p):#loops through the multiples and makes them false
        h[i] = False
    p+=1
    
  for i in range(2,n):
    if h[i]:
      primes.append(i)

  return primes


def twice_square(a):
  h = []
  for i in range(1,a):
    h.append(2*(i**2))
  return h

stuff = set()
for a in prime(100000):
  stuff.add(a)
  for b in twice_square(100):
    blah = int(a)+int(b)
    if blah % 2 != 0:
      stuff.add(blah)

for i in range(1,10000,2):
  if i not in stuff:
    print (i)

#prime(100000)#prints all primes under 40

print(time.time()-start)