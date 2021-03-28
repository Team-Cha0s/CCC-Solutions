#made my mohammed
number = int(input())
tide = input().split()

sum1 = 0

stack = []
for i in range(0, number):
    stack.append(tide[i])
for i in range(0, len(stack)): 
    stack[i] = int(stack[i]) 

for i in range(0, len(stack)):
        sum1 += int(stack[i])

average = sum1 / number

lowtide = []
hightide = []

for i in range(0, len(stack)):
    if stack[i] < average:
        lowtide.append(stack[i])
    else: 
        hightide.append(stack[i])

lowtide = sorted(lowtide, reverse=True)
hightide = sorted(hightide, reverse=False)

final = []
for i in range(0, len(lowtide) and len(hightide)):
    final.append(lowtide[i])
    final.append(hightide[i])

final = [str(int) for int in final]

my_string = " "
for a in final:
    my_string = my_string + ' ' + a
print(my_string.strip())







