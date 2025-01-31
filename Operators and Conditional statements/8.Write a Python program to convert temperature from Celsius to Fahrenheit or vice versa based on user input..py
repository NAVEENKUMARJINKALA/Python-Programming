def cel_fahren(cel):
    fahren=(cel*9/5)+32
    return fahren
#temp=float(input("enter a temp"))
#print(cel_fahren(temp))
def fah_cel(fah):
    cel=(fah-32)*5/9
    return cel
print(cel_fahren(100))
print(fah_cel(212))