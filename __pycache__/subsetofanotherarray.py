#Check if an array is subset of another array

def subArray(a,b):
    c={}
    if len(a)==0 or len(b)==0:
        return True
    else:
        sum=0
        for i in range(len(b)):
            c[b[i]]=0
        for j in range(len(a)):
            c[a[j]]=1
        for k in range(len(b)):
            if c[b[k]]==0:
                sum+=1
        print(c,sum)
        if sum!=0:
            return False
        else:
            return True
print(subArray([11, 1, 13, 21, 3],[11, 3,21,4] ))