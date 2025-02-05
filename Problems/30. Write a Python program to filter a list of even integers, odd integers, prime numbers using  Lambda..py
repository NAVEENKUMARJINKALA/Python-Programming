#30. Write a Python program to filter a list of even integers, odd integers, prime numbers using
#Lambda.
list_1=list(map(int,input("Enter a list of integers :").split()))

def getintegers(lst):
    evens=list(filter(lambda x: x%2==0,lst))
    odds=list(filter(lambda x: x%2!=0,lst))
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    primes = list(filter(is_prime, lst))
    return evens,odds,primes
print(getintegers(list_1))


