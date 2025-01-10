
'''
1.Program to declare and print a list
List=[10,20,30,40,'naveen','kumar']
print(type(List))
print(List)
print(List[0])
print(List[1])
print(List[-1])



#2. program to print list elements in different ways

List=[10,20,30,40,'naveen','kumar']
for i in List:   #For Loop
   print(i)
While Loop
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

#3. Program for Adding, removing elements in the list

list = ['apple', 'banana', 'cherry']
#print(list)
#print(type(list))
#list.append(400)
#print(list)
#list.insert(3,'naveen')
#print(list)
#list.append([50,100,150,200])
#print(list)
#list.pop()
#print(list)
#list.clear()
#print(list)
#del list[2]

#4. Program to print a list using 'FOR and IN' loop

for item in list:
    print(item)

print("apple" in list)
print(22 in list)
print(22 not in list)

'''''''
#5. Program to add an element at specified index in a list
Listt=['Today', 'is ','a ','day']
Listt.insert(3,'great')
print(Listt)

n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
print(10 in n)
fremove=int(input("enter a number"))
#7. Remove all occurrences a given element from the list

while fremove in n:
    n.remove(fremove)
    print(n)
print(10 in n)
print(n.count(50))


#8. Program to remove all elements in a range from the List
#n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
#for i in range(n):
 #   n.remove(i)
  #  print(i)
n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
rstart=10
rend=30
newlist=[item for item in n if not (rstart<=item >=rend )]
print(newlist)


#9. Program to sort the elements of given list in Ascending and Descending Order
#n=[10, 20, 30, 40, 50, 30, 60,10,50,10,10,10]
#list=sorted(n)
#print(list)
#n.sort(reverse=True)
#print(n)
#10. Program to find the differences of two lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
print(list1)
print(list2)
difference1= [item for item in list1 if item not in list2]
#print(difference1)

difference2=[item for item in list2 if item not in list1]
#print(difference2)

set1=set(list1)
set2=set(list2)
#print(set1,set2)
symmetric=list(set1 ^ set2)
print(symmetric)
S=sorted(symmetric)
print(S)

'''

