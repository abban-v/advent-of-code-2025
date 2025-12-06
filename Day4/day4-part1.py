file=open("input.txt")
layout=[]
movablerolls=0
for i in file.read().split('\n'):
    layout.append(i)
for i in range(len(layout)):
    for j in range(len(layout[i])):
        if layout[i][j]!="@":
            continue
        adjacentroll=0
        for k in range(i-1,i+2):
            if k<0 or k>len(layout)-1:
                continue
            for l in range(j-1,j+2):
                if l<0 or l>len(layout[i])-1:
                    continue
                if k==i and l==j:
                    continue
                if layout[k][l]=='@':
                    adjacentroll+=1
        if adjacentroll<4:
            movablerolls+=1
print(movablerolls)
