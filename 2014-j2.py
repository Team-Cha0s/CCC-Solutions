#made by mohammed
amnt = int(input())
votes = input()

listV = list(votes) 
ATeam = 0
BTeam = 0

for i in range(len(votes)):
    if listV[i] == "A":
        ATeam = ATeam + 1
    if listV[i] == "B":
        BTeam = BTeam + 1

if ATeam > BTeam:
    print("A")
elif ATeam < BTeam:
    print("B")
else:
    print("Tie")
