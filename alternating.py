def alternating(l):
    sum=1
    d=[]
    left=0
    right=1
    t=''
    while right < len(l) :
        t+=l[left]
        if int(l[left])%2 != int(l[right])%2:
            sum+=1
            left=right
            right+=1
        elif int(l[left])%2 == int(l[right])%2:
            d.append((sum,t))
            sum=1
            t=''
            left=right
            right+=1
            continue
    return t
print(alternating('1234'))