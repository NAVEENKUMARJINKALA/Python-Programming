'''
a=int(input(("enter any two digit number")))
print(a)
if a<100:
    #print("a is below hundred")
    str1=str(a)
    #print(str1)
    sm=int(str1[0])
    sm1=int(str1[1])
    fsum=sm+sm1
    print("total sum is",fsum)
  '''
#a=("naveen","25","9705740442")
#(name,age,mob)=a
#print(name)
#print(age)
a=[10,20,30,50,60]
def cursum(a):
    csum=0
    cmsum=[]
    for num in a:
        csum+=num
        cmsum.append(csum)
    print(cmsum)
print(cursum(a))
str1='hello_student'
str2=reversed(str1)
print(str2)