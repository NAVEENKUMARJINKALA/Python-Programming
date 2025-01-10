n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
fremove=10
while fremove in n:
    n.remove(fremove)
    print(n)
print(10 in n)
print(n.count(50))