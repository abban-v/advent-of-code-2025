file=open("input.txt")
rows=file.read().split('\n')
total=list()

max=0
intermediate=list()
for i in range(1,len(rows[0])+1):
    s=""
    for j in rows:
        s+=j[-i]
    s=s.strip()
    if s.isdigit():
        intermediate.append(int(s))
    elif s[:len(s)-1].strip().isdigit() and (s[len(s)-1]=="*" or s[len(s)-1]=="+"):
        intermediate.append(int(s[:len(s)-1].strip()))
        intermediate.append(s[len(s)-1])
        total.append(intermediate)
        intermediate=list()
sum=0
for i in total:
    op=i[-1]
    if op=="*":
        intermediate=1
    elif op=="+":
        intermediate=0
    for j in range(len(i)-1):
        if op=="*":
            intermediate*=i[j]
        elif op=="+":
            intermediate+=i[j]
    sum+=intermediate
print(sum)