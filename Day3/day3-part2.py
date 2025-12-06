file=open("input.txt","r")
l=file.read().split('\n')
sum=0
for i in l:
    nums=list(i)
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    jolts=""
    while len(jolts)<12:
        lengthnums=len(nums)
        element=max(nums[0:lengthnums+len(jolts)-11])
        jolts+=str(element)
        nums=nums[nums.index(element)+1:]
    sum+=int(jolts)
print(sum)