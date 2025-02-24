def sums(n):
    if n==1:
        return 1
    else:
        return n+sums(n-1)
print(sums(100))

def reverse(s):
    if len(s)==1:
        return s
    else:
        return s[-1] + reverse(s[0:len(s)-1])
print(reverse("yoyo master"))

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

def fibonacci(n):
    if n==0:
        return 
    elif n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7))

def test(n):
    t=int(n**0.5)
    if t==0 or n==2:
        return 'Prime'
    elif n%t==0 and t>1:
        return "composite"
    else:
        t-=1
        return test(t)
print(test(2))