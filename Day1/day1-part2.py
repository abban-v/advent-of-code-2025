a=open("input.txt","r")
l=a.read().split()
zerocount=0
position=50
for i in l:
    if i[0]=="L":
        oldposition=position
        position-=int(i[1:])
        if position<=0:
            if oldposition==0:
                pass
            else:
                zerocount+=1
            zerocount+=abs(position)//100
            position=(100-(abs(position)%100))%100
    elif i[0]=="R":
        oldposition=position
        position+=int(i[1:])
        if position>=100:
            if oldposition==100:
                zerocount+=position//100-1
            else:
                zerocount+=position//100
            position%=100
print(zerocount)