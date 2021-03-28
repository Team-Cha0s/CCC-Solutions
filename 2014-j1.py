# made by mohammed
s1 = int(input())
s2 = int(input())
s3 = int(input())
Total = s1 + s2 + s3
if Total == 180:
    if s1 == s2 or s2 == s3 or s1 == s3:
        variable = "Isosceles"
        if s1 == s2 == s3:
            variable = "Equilateral"
    else:
            variable = "Scalene"
else: 
            variable = "Error"

print(variable)