#DISCOVERED TO BE HELPFUL IN FINDING OUT PRIMES WITHOUT SPENDING TOO MUCH TIME

import time
start = time.time()

def prime(n):
  h = [True] * (n+1)
  p = 2
  while(p*p <= n):
    if(h[p] == True):#checks to see if that value is good
      for i in range(p*2,n+1,p):#loops through the multiples and makes them false
        h[i] = False
    p+=1
    
  for i in range(2,n):
    if h[i]:
      print(i)

prime(40)#prints all primes under 40

print(time.time()-start)
