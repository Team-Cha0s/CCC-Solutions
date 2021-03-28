# made by mohammed
wins = 0
loses = 0
loop = 1

while loop <=6:
  result = input()
  if result == "W":
    wins = wins + 1
  loop += 1

if wins == 5 or wins == 6:
  print("1")
elif wins == 3 or wins == 4:
  print("2")
elif wins == 1 or wins == 2:
  print("3")
else:
  print("-1")

