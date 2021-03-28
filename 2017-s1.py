# made by mohammed
days = int(input())

team1string = input().split()
team2string = input().split()

sum1 = 0
sum2 = 0

k = 0

for i in range(0, len(team1string)):
        sum1 += int(team1string[i])
        sum2 += int(team2string[i])
        if sum2 == sum1:
                k = i + 1

if sum2 != sum1 and k < 0:
        k = 0

print(k)

