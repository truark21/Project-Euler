import time
import string
start = time.time()

tots = 0
file = open("blah.txt")
temp = file.readline()
names = temp.translate(None, '"').split(',')
names.sort()
for i in range(len(names)):
  nums = [ord(char) - 96 for char in names[i].lower()]
  tots = tots + (sum(nums)*(i+1))
print(tots)
print(time.time()-start)