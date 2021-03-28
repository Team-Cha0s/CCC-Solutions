n = int(input())
k = int(input())


# Body

start = n

for i in range(1, k+1):
  n += start*10**i
print(n)
