duration = int(input())
counter = 0

half_days = duration // 720 
other_minutes = duration % 720 

for t in range(other_minutes + 1):
  #print("t={0:3d}".format(t))
  hour = t // 60
  if (hour == 0):
    hour = 12
  minute = t % 60
  
  # 4 digits
  hour_tens = hour // 10
  hour_ones = hour % 10

  minute_tens = minute // 10 
  minute_ones = minute % 10

  #print( "{0:1d} {1:1d} {2:1d} {3:1d}".format(hour_tens, hour_ones, minute_tens, minute_ones))
  
  if hour_tens == 1:
    if (hour_tens - hour_ones) == (hour_ones - minute_tens) and (hour_ones - minute_tens) == (minute_tens - minute_ones):
      counter = counter + 1
  else:
    if (hour_ones - minute_tens) == (minute_tens - minute_ones) :
      counter = counter + 1


total = half_days * 31 + counter 
print (total)

# sequences per day
#seq = 31
# how many days 
#days = duration / 720
# get the days until last day without the last day
#daysint = int(days)
# get the decimal place remainder 
#days = days - daysint
# convert the remainder to percentage
#percentage = "{:.0%}".format(days)
# get the amount of minutes that percentage values
# 

#counter = daysint * seq

