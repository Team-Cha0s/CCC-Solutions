# Problem J2: Occupy Parking

#Problem Description
#You supervise a small parking lot which has N parking spaces. 

#Yesterday, you recorded which parking spaces were occupied by cars and which were empty.

# Today, you recorded the same information


parking = int(input())
yesterday = input()
today = input()

counter = 0 # this is the counter thats gonna count the parking spaces occupied 

for i in range(parking):
  if yesterday[i] == today[i] == 'C':
    counter += 1
print(counter)
