n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
rstart=10
rend=30
newlist=[item for item in n if not (rstart<=item >=rend )]
print(newlist)