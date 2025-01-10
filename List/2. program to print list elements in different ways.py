
List=[10,20,30,40,'naveen','kumar']
for i in List:   #For Loop
   print(i)
#While Loop
index=0
while index<len(List):
    print(List[index])
    index+=1

#Using Range
List=[10,20,30,40,'naveen','kumar']
for i in range(len(List)):
    print(List[i])
#Using Map functions
str_list = ['apple', 'banana', 'cherry']
def usingmap(item):
    print(item)
list(map(usingmap,str_list))
