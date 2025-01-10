tuple2 = (10, 20, 30, 40, 50,60,70,80,90)
k=3
min_elements=sorted(tuple2)[:k]
print(min_elements)

max_elements=sorted(tuple2,reverse=True)[:k]
max_elements.sort()
print(max_elements)