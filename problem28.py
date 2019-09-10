import time
start = time.time()

sum1 = 0
topright = 0
topleft = 0
botleft = 0
botright = 0
for i in range(3,1003,2):
  topright = i**2
  botright = topright - ((i//2) * 6)
  botleft = topright - ((i//2) * 4)
  topleft = topright - ((i//2) *2)
  sum1 += topright + botright + botleft + topleft
print(sum1+1)

end = time.time()
print(end-start)