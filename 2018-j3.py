

ogdis = input().strip()
dis = list(map(int, ogdis.split(' ')))
table = [0] * 5


for i in range(1, 5):
  table[i] = table[i - 1] + dis[i - 1]

for i in range(5):
  for j in range(5):
   dis = table[j] - table[i]
   if dis < 0: 
       dis = dis * -1
   print(dis, end = " ")
  print("\n")
  