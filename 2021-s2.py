rows = int(input())
cols = int(input())

x = [0] * rows
y = [0] * cols

loop = int(input())

for i in range(loop):
    grid, pos = input().split()
    if grid == "C":
        y[int(pos) - 1] ^= 1
    elif grid == "R":
        x[int(pos) - 1] ^= 1
        

print(x.count(1) * len(y) + y.count(1) * len(x) - 2 * x.count(1) * y.count(1))