#problem 26leetcode:

def RemoveDuplicates(a):
    left=0
    right=1
    sum=0
    while right<len(a):
        if a[left]<a[right]:
            left=right
            right+=1
        else:
            sum+=1
            right+=1
    return len(a)-sum
print(RemoveDuplicates([0,0,1,1,1,2,2,3,3,4]))