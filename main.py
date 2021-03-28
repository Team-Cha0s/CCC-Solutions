import os
import time

def is_possible(input):
    hour = 12
    minute = 0
    counter = 0 

    for i in range (input):
        minute = int(minute)
        hour = int(hour)
        minute += 1 
        if minute >= 60:
            minute -= 60
        if hour + 1 < 13:
            hour += 1
        else:
            hour = (hour + 1) % 12
        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = minute 
        minute = str(minute)
        hour = str(hour)
        time = hour + minute
        if len(time) == 3:
            if (int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0])):
                counter += 1 
        else:
            if ((int(time[3]) - int(time[2])) == (int(time[2]) - int(time[1]))) and ((int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0]))):
                counter += 1 
        
        print(counter)

test_folder = r'Tests\2017\junior_data\j4'
test_files = os.listdir(test_folder)
#test_files = ['j5.02.02.in']
for file in test_files:
  if file.endswith('.in'):
    filename, ext = os.path.splitext(file)

    input_file_pathname = os.path.join(test_folder, file)
    input_file = open(input_file_pathname, 'r')

    output_file_pathname = os.path.join(test_folder, filename + '.out')
    output_file = open(output_file_pathname, 'r')

    input = int(input_file.readline()) 


 

    expected_output = output_file.readline().strip()
    start = time.time()
    result = is_possible(input)
    end = time.time()
    duration = end - start
    if result == expected_output:
      print(file, "passed in", duration, "s")
    else:
      print(file, "failed in", duration, "s")