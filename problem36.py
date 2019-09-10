import time
start = time.time()

total = 0
for x in range(1000000):
  temp = [int(i) for i in str(x)]
  temp1 = list(reversed(temp))
  if temp == temp1:
    new_temp = list('{0:b}'.format(x))
    new_temp1 = list(reversed(new_temp))
    if new_temp == new_temp1:
      total += x

print(total)

end = time.time()
print(end-start)