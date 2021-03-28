#made by mohammed
l1 = input().split()
l2 = input().split()
l3 = input().split()
l4 = input().split()

for i in range(4): 
    l1[i] = int(l1[i]) 
    l2[i] = int(l2[i]) 
    l3[i] = int(l3[i]) 
    l4[i] = int(l4[i]) 

suml1 = 0
suml2 = 0
suml3 = 0 
suml4 = 0
for i in range(4):
    suml1 = suml1 + l1[i]
    suml2 = suml2 + l2[i]
    suml3 = suml3 + l3[i]
    suml4 = suml4 + l4[i]
c1 = + l1[0] + l2[0] + l3[0] + l4[0]
c2 = + l1[1] + l2[1] + l3[1] + l4[1]
c3 = + l1[2] + l2[2] + l3[2] + l4[2]
c4 = + l1[3] + l2[3] + l3[3] + l4[3]

if suml1 != suml2:
    print("not magic")
elif suml1 != suml3:
    print("not magic")
elif suml1 != suml4:
    print("not magic")
elif suml2 != suml3:
    print("not magic")
elif suml2 != suml4:
    print("not magic")
elif suml3 != suml4:
    print("not magic")
elif c1 != c2:
    print("not magic")
elif c1 != c3:
    print("not magic")
elif c1 != c4:
    print("not magic")
elif c2 != c3:
    print("not magic")
elif c2 != c4:
    print("not magic")
elif c3 != c4:
    print("not magic")
else: 
    print("magic")