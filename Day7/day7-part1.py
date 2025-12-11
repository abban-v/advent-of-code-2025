file=open("input.txt")
rows=file.read().split("\n")
rowlength=len(rows[0])
for i in range(rowlength):
    if rows[0][i]=="S":
        startingindex=i

beamindexes=[startingindex]
count=0
for i in range(1,len(rows)):
    for j in range(rowlength):
        if (rows[i][j]=='^' and j in beamindexes):
            count+=1
            if j-1 not in beamindexes:
                beamindexes.append(j-1)
            if j+1 not in beamindexes:
                beamindexes.append(j+1)
            beamindexes.remove(j)
print(count)