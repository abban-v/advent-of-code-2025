file=open("input.txt")
rows=file.read().split("\n")
rowlength=len(rows[0])
for i in range(rowlength):
    if rows[0][i]=="S":
        startingindex=i
beamindexes={startingindex:1}
count=0
for i in range(1,len(rows)):
    newbeamindexes=dict()
    for j in range(rowlength):
        if (rows[i][j]=='^' and j in beamindexes and beamindexes[j]>0):
            if j-1 not in beamindexes:
                if j-1 not in newbeamindexes:
                    newbeamindexes[j-1]=beamindexes[j]
                else:
                    newbeamindexes[j-1]+=beamindexes[j]
            else:
                beamindexes[j-1]+=beamindexes[j]
            if j+1 not in beamindexes:
                if j+1 not in newbeamindexes:
                    newbeamindexes[j+1]=beamindexes[j]
                else:
                    newbeamindexes[j+1]+=beamindexes[j]
            else:
                beamindexes[j+1]+=beamindexes[j]
            beamindexes[j]=0
    beamindexes.update(newbeamindexes)
    for k in range(rowlength):
        if k in beamindexes and beamindexes[k]==0:
            del beamindexes[k]
for i in beamindexes:
    count+=(beamindexes[i])
print(count)