def reverse(s):
    t={}
    r=''
    n=len(s)
    for i in range(n):
        t[n-i-1]=s[i]
    for k in range(n):
        r+=t[k]
    return r
print(reverse("hiiiiii"))