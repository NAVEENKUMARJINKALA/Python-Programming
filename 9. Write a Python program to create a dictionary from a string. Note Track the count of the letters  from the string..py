str1='Helloworld'
str2='hellonaveen'
lcount={}
#def dictsr(str):
#    for char in str:
#        if char.isalpha():
#            char=char.lower()
#            if char in lcount:
#                lcount[char]+=1
#            else:
#                lcount[char]=1
#    return lcount
#print(dictsr(str2))
'''
def dis(str):
    for char in str1:
        if char.isalpha():
            char=char.lower()
            if char in lcount:
                lcount[char]+=1
            else:
                lcount[char]=1
    return lcount
print(dis(str1))
str5='Hello Naveen Kumar'
print(str5)
print(str5.split(","))
print(str5.strip())
rev=str5[::-1]
print("reversed string" ,rev)
'''


#str=input("enter a string including commas")
#strrev=str[::-1]
#if str==strrev:
#    print("its a palindrome")
#else:
 #   print("not a palindrome")
#
#for i in range(100):
 #   if i**2==16:
#        print(i)
'''
num =list()
current_sum =0
cummulative_sum = []
for item in num:
    current_sum+=item
    cummulative_sum.append(current_sum)
#print(current_sum)
print(cummulative_sum)

'''


def num_to_words(n):
    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return ones[num]
        elif num < 100:
            return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ones[num // 100] + " hundred" + (" " + helper(num % 100) if num % 100 != 0 else "")

    result = ""
    if n >= 1000:
        result += helper(n // 1000) + " thousand" + (" " if n % 1000 != 0 else "")
        n %= 1000

    result += helper(n)
    return result.strip()


# Example usage
num = int(input("Enter a number: "))
print(f"The number {num} in words is: {num_to_words(num)}")

