idranges=input("Enter product ranges: ")
idranges_list=idranges.split(',')
sum=0
for i in idranges_list:
    eachrange=i.split('-')
    for j in range(int(eachrange[0]),int(eachrange[1])+1):
        current_id=str(j)
        mid=len(current_id)//2
        pattern=False
        for k in range(1,mid+1):
            subpattern=current_id[:k]
            if len(current_id)%len(subpattern)!=0:
                continue
            pattern=False
            if current_id==subpattern*(len(current_id)//len(subpattern)):
                sum+=int(current_id)
                break
print(sum)