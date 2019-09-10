import time
start = time.time()

months = [0,31,59,90,120,151,181,212,243,273,304,334]
months_leap = [0,31,60,91,121,152,182,213,244,274,305,335]

year_start = 1901
day_start =  2
sundays_count = 0

while year_start <= 2000:
  if year_start % 4 != 0 or year_start % 400 == 0:
    year = [0 if i % 7 != 0 else 1 for i in range(day_start,365+day_start) ]
    for j in range(len(months)):
      if year[months[j]] == 1:
        sundays_count+=1

  else:
    year = [0 if i % 7 != 0 else 1 for i in range(day_start,366+day_start) ]
    for j in range(len(months)):
      if year[months_leap[j]] == 1:
        sundays_count+=1
        year[months_leap[j]] = 2
    day_start +=1
  day_start+=1
  year_start +=1

print(sundays_count)
print(time.time() - start)