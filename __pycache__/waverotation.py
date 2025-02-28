#Define a function that defines a wave rotation
def WaveRotation(l):
    left=0
    right=1
    while right<len(l):
        if left%2==0:
            if l[left] > l[right]:
                left+=1
                right+=1
            else:
                l[left],l[right]=l[right],l[left]
        else:
            if l[left] < l[right]:
                left+=1
                right+=1
            else:
                 l[left],l[right]=l[right],l[left]
    return l

print(WaveRotation([1,2,0,3,4,5,6,7,8,10]))