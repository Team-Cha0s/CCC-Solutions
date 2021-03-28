#Apples scored 10 · 3 + 3 · 2 + 7 · 1 = 43 points
#Bananas scored 8 · 3 + 9 · 2 + 6 · 1 = 48 points
# points are the number of each type of score (1,2,3)

a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

aTotal = 3 * a3 + 2 * a2 + a1  
bTotal = 3 * b3 + 2 * b2 + b1

if aTotal > bTotal:
  print ("A")
elif bTotal > aTotal:
  print ("B")
else:
  print ("T")

