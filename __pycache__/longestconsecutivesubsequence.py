#Given an array of integers, the task is to find the length of the longest subsequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 
#Idea1
def LCS(a):
    if len(a)==0 or len(a)==1:
        return len(a)
    hashset=set()
    sum2,max2=1,0
    j=min(a)
    for i in range(len(a)):
        hashset.add(a[i])
    for k in hashset:
        if k+1 in hashset:
            sum2+=1
        else:
            if sum2>max2:
                max2=sum2
            sum2=1
    return max(max2,sum2),hashset
print(LCS([0,-1,1]))
#Idea2

def LCS2(a):
    if len(a)==0 or len(a)==1:
        return len(a)
    hashset=set()
    sum2,max2=1,0
    j=min(a)
    for i in range(len(a)):
        hashset.add(a[i])
    for k in hashset:
        if k+1 in hashset:
            sum2+=1
        else:
            if sum2>max2:
                max2=sum2
            sum2=1
    return max(max2,sum2),hashset