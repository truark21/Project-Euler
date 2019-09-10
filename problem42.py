import time
start = time.time()
j = 0
triangleList = []

def triangle(x):
  return int(.5*x*(x+1))
  
def StringToValue(y):
  return sum([ord(char) - 96 for char in y.lower()])

for i in range(0,20):
  triangleList.append(triangle(i))


file = open("words.txt","r")
currentline = []
for line in file:
  currentline = line.split(",")
for x in currentline:
  word_value = StringToValue(x.strip("\""))
  if word_value in triangleList:
    j+=1
print(j)

end = time.time()
print(end-start)