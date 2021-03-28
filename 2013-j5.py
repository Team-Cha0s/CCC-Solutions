team = int(input())
games = int(input())

t1S = 0
t2S = 0
t3S = 0
t4S = 0

t1M= 0
t2M = 0
t3M = 0
t4M = 0

win = 3
tie = 1
loss = 0

outcomes = 18

for i in range(games):
    line = input().split()
    line = [int(i) for i in line]
    #[1, 3, 7, 5]
    if line[0] == 1:
        t1M = t1M + 1
        
        if line[1] == 2:
            t2M = t2M + 1
            if line[2] > line[3]:
                t1S = t1S + win
                outcomes = outcomes - 3
            elif line[2] < line[3]:
                t2S = t2S + win
                outcomes = outcomes - 3
            if line[2] == line[3]:
                t1S = t1S + tie
                t2S = t2S + tie
                outcomes = outcomes - 3
        
        if line[1] == 3:
            t3M = t3M + 1
            if line[2] > line[3]:
                t1S = t1S + win
                outcomes = outcomes - 3
            elif line[2] < line[3]:
                t3S = t3S + win
                outcomes = outcomes - 3
            if line[2] == line[3]:
                t1S = t1S + tie
                t3S = t3S + tie
                outcomes = outcomes - 3
        
        if line[1] == 4: 
            t4M = t4M + 1
            if line[2] > line[3]:
                t1S = t1S + win
                outcomes = outcomes - 3
            elif line[2] < line[3]:
                t4S = t4S + win
                outcomes = outcomes - 3
            if line[2] == line[3]:
                t1S = t1S + tie
                t4S = t4S + tie
                outcomes = outcomes - 3

    if line[0] == 2: 
        t2M = t2M + 1
        
        if line[1] == 3:
            t3M = t3M + 1
            if line[2] > line[3]:
                t2S = t2S + win
                outcomes = outcomes - 3
            elif line[2] < line[3]:
                t3S = t3S + win
                outcomes = outcomes - 3
            if line[2] == line[3]:
                t2S = t2S + tie
                t3S = t3S + tie
                outcomes = outcomes - 3
            
        if line[1] == 4: 
            t4M = t4M + 1
            if line[2] > line[3]:
                t2S = t2S + win
                outcomes = outcomes - 3
            elif line[2] < line[3]:
                t4S = t4S + win
                outcomes = outcomes - 3
            elif line[2] == line[3]:
                t2S = t2S + tie
                t4S = t4S + tie
                outcomes = outcomes - 3

    if line[0] == 3:      
        t3M = t3M + 1
        
        if line[1] == 4: 
            t4M = t4M + 1
            if line[2] > line[3]:
                t3S = t3S + win
                outcomes = outcomes - 3
            elif line[2] < line[3]:
                t4S = t4S + win
                outcomes = outcomes - 3
            if line[2] == line[3]:
                t3S = t3S + tie
                t4S = t4S + tie
                outcomes = outcomes - 3


if team == 1:
    if t1S == 0 and t1M > 2:
        print(t1S)
if team == 2:
    if t2S == 0 and t2M > 2:
        print(t2S)
if team == 3:
    if t3S == 0 and t3M > 2:
        print(t3S)
if team == 4:
    if t4S == 0 and t4M > 2:
        print(t4S)
    

