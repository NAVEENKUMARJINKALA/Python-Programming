Tupledigits=[(10,20,30),(10,20),(50,60,70,80,90),(58,68,78,98)]
empty=[]
for tup in Tupledigits:
    for num in tup:
        if isinstance(num,int):
            empty.append(num)
print(empty)