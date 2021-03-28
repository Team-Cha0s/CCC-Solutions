import math

def split(word): 
    return [char for char in word]  
string = input()
sortedL = sorted(string)
string = split(string)
counter = 0

for x in range(len(sortedL)):
    if string[x] != sortedL[x]:
        counter = counter + 1
    
print(math.ceil(counter/2))