#made by mohammed
var1 = int(input())
var2 = int(input())

country1 = [int(x) for x in input().split()]
country2 = [int(x) for x in input().split()]

country1.sort()
country2.sort() 

if var1 == 1:
    var = -1 
else:
    0

sum1 = 0 

for k in range(var2):
    sum1 += max(country1.pop(-1), country2.pop(var))
        
print(sum1)