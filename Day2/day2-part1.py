idranges=input("Enter product ranges: ")
idranges_list=idranges.split(',')
sum=0
for i in idranges_list:
    eachrange=i.split('-')
    for j in range(int(eachrange[0]),int(eachrange[1])+1):
        current_id=str(j)
        mid=len(current_id)//2
        if current_id[:mid]==current_id[mid:]:
            sum+=int(current_id)
print(sum)