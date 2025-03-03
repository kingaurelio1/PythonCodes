#Problem 3467 leetcode

def TransformArrayParity(a):
    counter=0
    pointer1=0
    pointer2=0
    while pointer1 < len(a):
        if a[pointer1]%2==0:
            counter+=1
            pointer1+=1
        else:
            pointer1+=1
    while pointer2 < len(a):
        if counter>0:
            a[pointer2]=0
            pointer2+=1
            counter-=1
        else:
            a[pointer2]=1
            pointer2+=1
    return a
print(TransformArrayParity([1,3,5]))