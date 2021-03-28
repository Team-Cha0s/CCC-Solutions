#made by mohammed
amount = int(input())
player1 = 100
player2 = 100

for i in range(amount):
    roll = input()
    roll1 = roll.split()
    roll1 = [int(i) for i in roll1] 
    if roll1[0] > roll1[1]:
        player1 = player1 - roll1[0]
    if roll1[0] < roll1[1]:
        player2 = player2 - roll1[1]

print(player2)
print(player1)
