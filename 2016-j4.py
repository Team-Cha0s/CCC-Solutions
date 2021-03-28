#made by mohammed
input1 = input()
min_from_hour = int(input1[0]+input1[1])*60
min_from_min = int(input1[3] + input1[4])
min = min_from_hour + min_from_min

counter = 0

peakhours1 = range(420, 600)
peakhours2 = range(900, 1140)

if input1 == "07:00":
    print("10:30")
elif input1 == "15:00":
    print("19:30")
else:
    while counter < 6:
        if min == 1440:
            min = 0

        if min in range(420, 600) or min in range(900, 1140):
            min += 40
        else:
            min += 20

        counter += 1

    hour = min/60
    new_min = min%60
    hour = int(hour)
    if hour < 10:
        hour = '0' + str(hour)
    if hour == 24:
        hour == 0
    if new_min == 0:
        if len(str(hour)) == 1:
            print('0' + str(hour) + ":" + "00")
        else:
            print(str(hour) + ":" + "00")
    else:
        if len(str(hour)) == 1:
            print('0' + str(hour) + ":" + str(new_min))
        else:
            print(str(hour) + ":" + str(new_min))