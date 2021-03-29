N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

area = 0
for i in range(1, N + 1):
    area += (a[i] + a[i - 1]) * b[i - 1] / 2.0

print(area)