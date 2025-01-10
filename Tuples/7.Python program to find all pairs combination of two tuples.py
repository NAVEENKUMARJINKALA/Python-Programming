#Tlist=[(10,20,30),(10,20),(50,60,70,80,90),(58,68,78,98)]
#Tupledigits=[(10,20,30),(10,20),(50,60,70,80,90),(58,68,78,98)]
Tlist=[(10,20),(30,40),(50,60)]
Tupledigits=[(70,80),(10,20),(30,40),(50,60)]
pairs=[]
for tu1 in Tlist:
    for tu2 in Tupledigits:
        pairs.append((tu1,tu2))

print(pairs)