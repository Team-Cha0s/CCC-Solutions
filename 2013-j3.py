year = input()
temp = int(year) + 1
year = str(temp)


def distinct(year):
    y = str(year)
    for digit in y:
        if y.count(digit) > 1:
            return(False)
    return(True)
    
    
    
while not distinct(year):
    year = int(year)
    year = year + 1
print(year)
