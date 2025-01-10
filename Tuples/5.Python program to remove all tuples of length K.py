
k=4
Tlist=[(10,20,30),(10,20),(50,60,70,80,90),(58,68,78,98)]
flist=[tup for tup in Tlist if len(tup)!=k]
print(flist)