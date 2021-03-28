time = int(input())
amount = int(input())
chores = []
completed = []

for i in range(amount):
    chores.append(int(input()))

chores.sort()
Time1 = time
for i in range(len(chores)):
    if chores[i] <= Time1:
        completed.append(chores[i])
        Time1 = Time1 - chores[i]

print(len(completed))        
            

    