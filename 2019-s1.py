# made by mohammed
rotate = str(input())

V = 0
H = 0

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

temp = stack


for i in range(0, len(rotate)):
    if(rotate[i] == 'V'):
        V = V + 1
    elif(rotate[i] == 'H') :
        H = H + 1

count = 0

while count != H:
    stack[0], stack[2] = stack[2], stack[0]
    stack[1], stack[3] = stack[3], stack[1]
    count = count + 1

count = 0

while count != V:
    stack[0], stack[1] = stack[1], stack[0]
    stack[2], stack[3] = stack[3], stack[2]
    count = count + 1


print(str(stack[0]) + " " + str(stack[1]))
print(str(stack[2]) + " " + str(stack[3]))