#made by mohammed
string = input()
answer = input()

list = []

for i in range(len(answer)):
    list.append(answer[i:]+answer[:i])

state = 0

for s in list:
    if s in string:
        state = 1
        break

if state == 0:
    print("no")
else:
    print("yes")