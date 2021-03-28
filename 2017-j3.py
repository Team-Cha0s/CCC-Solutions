ai, bi = input().split()
ci, di = input().split()
t = int(input())

a, b = int(ai), int(bi)
c, d = int(ci), int(di)

Distance = 0
Difference = 0
# Vertical
if a>c:
  Distance += a - c
else:
  Distance += c - a


# Horizontal 
if b>d:
  Distance += b - d
else:
  Distance += d - b

if t == Distance:
  print("Y")
else:
  if (t>Distance):
    Difference = t - Distance 
    
    if (Difference % 2 == 0):
      print ("Y")
      
    else:
      print ("N")
  
  else: 
    print("N")
