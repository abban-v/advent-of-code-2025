file=open("input.txt")
freshids=file.read().split('\n')
fresh=dict()
for i in freshids:
    if i=='':
        break
    ranges=i.split('-')
    ranges[0]=int(ranges[0])
    ranges[1]=int(ranges[1])
    if ranges[0] in fresh:
        if ranges[1]>fresh[ranges[0]]:
            pass
        else:
            continue
    fresh[ranges[0]]=ranges[1]
freshlist=list()
for i in fresh.items():
    freshlist.append(list(i))
fresh=freshlist
fresh.sort(key=lambda x: x[0])
for i in fresh:
    if i[1]==0:
        continue
    for j in fresh:
        if j[1]==0:
            continue
        if i[0]<=j[0]<=i[1]:
            if i[0]==j[0] and i[1]==j[1]:
                continue
            if j[1]>i[1]:
                i[1]=j[1]
                j[1]=0
            else:
                j[1]=0
freshcount=0
for i in fresh:
    if i[1]==0:
        continue
    freshcount+=(i[1]-i[0]+1)
print(freshcount)