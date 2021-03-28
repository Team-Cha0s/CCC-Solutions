number = int(input())
number = [int(x) for x in str(number)]
sum = number[0] + number[1] + number[2] + number[3] + number[4]
direction = 0
sum1 = 0

while sum != 45:
    sum1 = number[0] + number[1]
    if (sum1 == 0):
        print(previous + str(number[2]) + str(number[3]) + str(number[4]))
    elif (sum1 % 2) == 0:
        print("right " + str(number[2]) + str(number[3]) + str(number[4]))
        previous = "right "
    elif (sum1 % 2) == 1:  
        print("left " + str(number[2]) + str(number[3]) + str(number[4]))
        previous = "left "
    number = input()
    number = [int(x) for x in str(number)]
    sum = number[0] + number[1] + number[2] + number[3] + number[4]