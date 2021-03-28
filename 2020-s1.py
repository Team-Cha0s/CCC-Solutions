#made by marwan and mohammed
from operator import itemgetter

#done
n = int(input())
m = []

#done
for i in range(n):
    line = input().split()
    line = [int(i) for i in line]
    m.append(line)

a = m
m = sorted(a)

PP = m[0][1] #100
PT = m[0][0] #0
max_speed = 0
for i in range(len(m) - 1):
    if m[i+1][1] < PP:
        temp_speed = (PP - m[i + 1][1] ) / (m[i + 1][0] - PT) 
    else:
        temp_speed = (m[i + 1][1] - PP) / (m[i + 1][0] - PT) 
    PT = m[i + 1][0]
    PP = m[i + 1][1]
    if temp_speed > max_speed:
        max_speed = temp_speed
        

print(max_speed)
