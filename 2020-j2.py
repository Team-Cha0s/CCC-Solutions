p = int(input())
n = int(input())
r = int(input())
total = n
new_infections = n
day = 0
while (True):
  #print("new infections on day"+ str(day) + ": " + str(new_infections))
  #print("total:" + str(total))

  if total > p:
    print(day)
    break
  
  new_infections = new_infections*r

  total += new_infections
  
  day += 1
  
