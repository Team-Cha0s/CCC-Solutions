flowers = int(input())
measurements = []
for i in range(flowers):
    measurements.append(list(map(int, input().split())))

#print(measurements)

min_number = measurements[0][0]
row = 0
column = 0

if measurements[0][flowers-1] < min_number:
    row = 0
    column = flowers - 1
    min_number = measurements[0][flowers - 1]
if measurements[flowers-1][0] < min_number:
    row = flowers - 1
    column = 0
    min_number = measurements[flowers - 1][0]
if measurements[flowers-1][flowers-1] < min_number:
    row = flowers - 1
    column = flowers - 1
    minNumber = measurements[flowers - 1][flowers - 1]
    
if row == 0 and column == 0:  
    for i in range(flowers):
        for j in range(flowers):
            print(measurements[i][j], end=" ")
        print()

elif row == 0 and column > 0: 
    for i in range(flowers - 1, -1, -1):
        for j in range(flowers):
            print(measurements[j][i], end=" ")
        print()
            
elif row > 0 and column > 0:  
    for i in range(flowers - 1, -1, -1):
        for j in range(flowers - 1, -1, -1):
            print(measurements[i][j], end=" ")
        print()
else: 
    for i in range(flowers):
        for j in range(flowers - 1, -1, -1):
            print(measurements[j][i], end=" ")
        print()
        
