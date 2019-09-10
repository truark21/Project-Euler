import time
start = time.time()


tot = 400002
for n in range(10000,20000,2):
  l = [0] * (n/2)
  r = [1] * (n/2)
  k = l+r
  c=[]
  b = 0
  h = 0
  if n % 100 == 0:
    print(n)
  while k!=c:
    c = []
    for i in range(0,n):
      if i % 2 == 0:
        c.append(l[b])
      else:
        c.append(r[b])
        b+=1
    if k == c and h == 59:
      tot +=n
      print(tot,n)
    if k!= c and h == 59:
      c = k
    b=0
    h+=1
    l = c[0:n/2]
    r = c[n/2:]
  


print(time.time()-start)