#made by mohammed
month = int(input())
day = int(input())



if day == 18 and month == 2:
    print("Special")
elif month == 1 or (day < 18 and month == 2):
   print("Before")
else: 
    print("After")