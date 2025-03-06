#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

def Reverse(a):
    left=0
    right=len(a)-1
    while left<=right:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1
    return a
print(Reverse(["H","a","n","n","a","h"]))