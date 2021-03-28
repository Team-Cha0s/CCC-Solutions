b = int(input())

p = 5*b-400

print(p)
 
if p < 100:
    result = 1
elif p == 100:
    result = 0
elif p > 100:
    result = -1


print (result)