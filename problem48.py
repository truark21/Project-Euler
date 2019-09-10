import time
start = time.time()

total = 0
for x in range(1,1001):
  total += x**x
total=list(str(total))
for y in range(1,11):
  print(total[-11+y])
end = time.time()
print(end-start)