"""def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
def check_primes(lst):
    return all(is_prime(num) for num in lst)
lst=eval(input("enter a list of numbers:"))
print(check_primes(lst))"""

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
def checkprime(lst):
    return all(prime(num) for num in lst)
lst=eval(input("enter a number"))
print(checkprime(lst))


"""def prime1(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True
#print(prime1(5))"""