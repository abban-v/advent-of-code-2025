a=open("input.txt","r")
l=a.read().split()
zerocount=0
position=50
for i in l:
    if i[0]=="L":
        position-=int(i[1:])
        if position<0:
            position=100-(abs(position)%100)
    elif i[0]=="R":
        position+=int(i[1:])
        if position>=100:
            position%=100
    if position==0 or position==100:
        zerocount+=1
print(zerocount)
