tupl1=('naveen','kumar',20,30,500)

List=['Today','Tomorow','Yesterday']
print(List)
List.extend(list(tupl1))
print(List)

Newtuple=tupl1+tuple(List)
print(Newtuple)
