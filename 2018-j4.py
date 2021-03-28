table = [[*map(int, input().split())] 
for i in range(int(input()))]

low = min(map(min, table))

while low != table[0][0]:
    table = [*zip(*table[::-1])]

for i in table:
    print(" ".join(map(str, i)))