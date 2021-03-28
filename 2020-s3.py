from itertools import permutations

str1 = input()
perms = [''.join(p) for p in permutations(str1)]
perms = list(set(perms))
#print(perms)
str2 = input()
#points = 0
#for i in range(len(perms)):
#   if perms[i] in str2:
#        points = points + 1
        
#print(points)
print(sum(substring in str2 for substring in perms))


