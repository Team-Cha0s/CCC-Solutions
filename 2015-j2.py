#made by mohammed
string = str(input())

h = string.count(":-)")
s = string.count (":-(")

total = h + s

if total == 0:
    print("none")
elif h == s:
    print("unsure")
elif h > s:
    print("happy")
else:
    print("sad")
