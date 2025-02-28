#Given an array arr consisting of N integers and an integer K, the task is to insert an adjacent K for every occurrence of it in the original sequence and then truncate the array to the original length using an O(1) auxiliary space.
def insert(l,k):
    i=0
    j=0
    m=[]
    count=0
    while i<len(l):
        print(l)
        if l[i]!=k:
            i+=1
        else:
            count+=1
            l.pop()
            i+=1
    for k in range(count):
        l.append(0)
    while j < len(l):
        print(j,l)
        if l[j]==k:
            l.pop()
            l=l[0:j+1]+[0]+l[j+1::]
            j+=1
        else:
            j+=1
    
    
    return l
print(insert([1, 0, 2, 3, 0, 4, 5, 0],0))
    