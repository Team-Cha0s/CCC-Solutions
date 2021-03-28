#made by mohammed
string = ''
letters = 'abcdefghijklmnopqrstuvwxyz'
const = 'bcdfghjklmnpqrstvwxyz'
in1 = input()

list = []

for j in range(len(in1)):
        list.append(in1[j])
for i in range(len(list)):
    if list[i] in 'aeiou':
        string += list[i]
    elif list[i] == 'z':
        string += 'zuz'
    else:
        index = const.find(list[i])
        third = const[index + 1]
        first = list[i]
        if list[i] in 'bc':
            second = 'a'
        elif list[i] in 'dfg':
            second = 'e'
        elif list[i] in 'hjkl':
            second = 'i'
        elif list[i] in 'mnpqr':
            second = 'o'
        else:
            second = 'u'
        string = string + first + second + third
print(string)
