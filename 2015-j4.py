# made by mohammed
inp = int(input())
w = [0]*101
r = [0]*101
s = [0]*101
time = 0
for i in range(inp):
    ss = input().split()
    cmd = ss[0]
    n = int(ss[1])
    if cmd == 'S':
        w[n] += time - s[n]
        r[n] = 1
    elif cmd == "R":
        r[n] = -1
        s[n] = time
    else:
        time += n-2
    time += 1
for j in range(101):
    if r[j] != 0:
        if r[j] > 0:
            print(j, w[j])
        else:
            print(j, r[j])
