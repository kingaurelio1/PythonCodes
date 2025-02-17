def reverseStr(s):
    left=0
    right=len(s)-1
    t=True
    w=s.lower()
    while left <= right:
        if w[left]==w[right]:
            left+=1
            right-=1
        else:
            t=False
            break
    return t
print(reverseStr("Malayalam"))