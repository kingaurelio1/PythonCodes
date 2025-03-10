#Given an array arr[], write a function that segregates even and odd numbers. The functions should put all even numbers first, and then odd numbers.

def evenodd(a):
    evens=[]
    odd=[]
    for i in range(len(a)):
        if a[i]%2==0:
            evens.append(a[i])
        else:
            odd.append(a[i])
    l,r=0,0
    while l < len(evens):
        a[l]=evens[l]
        l+=1
    while r < len(odd):
        a[l+r]=odd[r]
        r+=1
    return a
print(evenodd([2,4,0]))