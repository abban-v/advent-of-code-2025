file=open("input.txt","r")
l=file.read().split('\n')
sum=0
for i in l:
    nums=list(i)
    for j in range(0,len(nums)):
        nums[j]=int(nums[j])
    maxnum=max(nums)
    maxindex=nums.index(maxnum)
    try:
        leftmax=max(nums[:maxindex])
    except:
        leftmax=0
    try:
        rightmax=max(nums[maxindex+1:])
    except:
        rightmax=0
    if leftmax>rightmax:
        if maxindex+1!=len(nums):
            jolts=str(maxnum)+str(rightmax)
        else:
            jolts=str(leftmax)+str(maxnum)
    else:
        jolts=str(maxnum)+str(rightmax)
    sum+=int(jolts)
print(sum)