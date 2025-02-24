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
print(reverse('abcd'))