number = int(input())

names = []

bids = []

for i in range(number):
    name = input()
    bid = int(input())
    scores.append(bid)
    names.append(name)

highbid = bids.index(max(bids))

print(names[highbid])
