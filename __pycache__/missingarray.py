#You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

def missing(a):
    counter=0
    n=len(a)
    m=((n+1)*(n+2))//2
    for i in range(len(a)):
        counter+=a[i]
    return m - counter
print(missing([1]))
