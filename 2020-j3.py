#made by mohammed

first = int(input())
drops = []

for i in range(first):
    drop = {}
    dropinput = list(map(int, input().split(',')))
    drop['x'] = dropinput[0]
    drop['y'] = dropinput[1]
    drops.append(drop)

lowX = None
highX = None
lowY = None
highY = None

for co in drops:
    x = co['x']
    y = co['y']

    if not lowX or x < lowX:
        lowX = x
    if not highX or x > highX:
        highX = x
    if not lowY or y < lowY:
        lowY = y
    if not highY or y > highY:
        highY = y

print(str(lowX - 1)+ ',' + str(lowY - 1))
print(str(highX + 1)+ ',' + str(highY + 1)) 