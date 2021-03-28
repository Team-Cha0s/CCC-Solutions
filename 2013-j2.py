string = input()
rotate = "IOSHZXN"

final = "YES"

for i in string:
    if i not in rotate:
        final = "NO"
        break
print(final)
