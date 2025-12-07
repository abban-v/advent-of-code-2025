file=open("input.txt")
freshids=file.read().split('\n')
checkids=freshids[freshids.index('')+1:]
freshids=freshids[:freshids.index('')]
fresh=dict()
for i in freshids:
    ranges=i.split('-')
    ranges[0]=int(ranges[0])
    ranges[1]=int(ranges[1])
    if ranges[0] in fresh:
        if ranges[1]>fresh[ranges[0]]:
            pass
        else:
            continue
    fresh[ranges[0]]=ranges[1]
freshcount=0
for i in checkids:
    idint=int(i)
    for key in fresh:
        if key<=idint<=fresh[key]:
            freshcount+=1
            break
print(freshcount)