sample_list = [(10, 20, 40), (40, 50, 60), (30, 80, 90)]
newlist=[(10, 20, 40), (30, 80, 90), 58, 25, 'sai']
newlist1=sample_list+newlist
#print(newlist1)
sample_list.append(58)
sample_list.extend([25,'sai'])
sample_list.insert(6,'naveen')
#print(sample_list)

sample_list.remove(sample_list[1])
#print(sample_list)
sample_list.pop(5)
#print(sample_list)
sample_list.clear()
#print(sample_list)
nums=[10,20,5,80,69,89]
def find_index(nums, target):
    return nums.index(target) if target in nums else -1

#print(find_index(nums,69))

def findex(list,target):
    if target in list:
        return list.index(target)
    else:
        print("out of index")
#print(findex(nums,100))

#def seven(start,end):
 #   return [num for num in range([start, end+1]) if num%2==0]
#print(seven(2,10))
start=2
end=10
def sevenn(start,end):
    for i in range(start,end):
        if i%2==0:
            print(i)
#jnk=print(sevenn(2,100))
def feveodds(nums):
    even=[num for num in nums if num%2==0]
    odds=[num for num in nums if num%2!=0]
    return even,odds
#print(feveodds(nums))

def csum(nums):
    crsum=0
    cum_sum=[]
    for num in nums:
        crsum+=num
        cum_sum.append(crsum)
    print(cum_sum)
    print(crsum)

#print(nums)

def nremv(list1,n):
    if n<=len(list1):
        return list1[:n]+list1[n+1:]

#print(nremv(nums,2))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
jnk=[*list1, *list2]
#print(jnk)
mrlist=list1[:]
for item in list2:
    mrlist.append(item)
#print(mrlist)


#Write a Python program to check if a number entered by the user is even or odd.
#number=int(input("Enter any number"))
#if number%2==0:
    #print("num is even")
#else:
    #print("num is odd")

#Write a Python program to swap the values of two variables without using a temporary variable.
a=10
b=20
a,b=b,a
#print(a)
x=[2,4,6,8]
a='123enKumar'
def strk(str):
    if str.isalpha():
        print("is a alpha")
#print(strk(a))



a=10
a+=32
print(x[:-1])
print(a)
lst=[500,250,6,99,582]
def lmax(lst):
    return min(lst)
print(lmax(lst))


