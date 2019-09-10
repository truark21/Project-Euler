import time
start = time.time()

alist = []
infile = open("file.txt","r")
for x in infile:
  alist.append(x.split())
while len(alist) > 1:
  back = alist.pop()
  spot = len(alist)
  for x in range(len(alist)):
    one = int(alist[-1][x]) + int(back[x])
    two = int(alist[-1][x]) + int(back[x+1])
    if one > two:
      alist[-1][x] = one
    else:
      alist[-1][x] = two
    if one > two and len(alist) == 1:
      print("done",one)
    elif two > one and len(alist) == 1:
      print("done",two)
    


end = time.time()
print(end-start)