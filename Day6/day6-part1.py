file=open("input.txt")
rows=file.read().split('\n')
total=list()

for i in rows:
    listnums=list()
    s=""
    for j in range(len(i)):
        if i[j]==" ":
            if s.isdigit():
                listnums.append(int(s))
            elif not s or s.isspace():
                s=''
                continue
            else:
                listnums.append(s)
            s=""
            continue
        s+=i[j]
    else:
        if s.isdigit():
            listnums.append(int(s))
        elif not s or s.isspace():
            pass
        else:
            listnums.append(s)
    total.append(listnums)
sum=0
for i in range(len(total[0])):
    op=total[-1][i]
    if op=="*":
        intermediate=1
    else:
        intermediate=0
    for j in range(len(total)-1):
        if op=="*":
            intermediate*=total[j][i]
        elif op=="+":
            intermediate+=total[j][i]
    sum+=intermediate
print(sum)