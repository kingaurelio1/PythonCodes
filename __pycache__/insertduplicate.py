#Given an array arr consisting of N integers and an integer K, the task is to insert an adjacent K for every occurrence of it in the original sequence and then truncate the array to the original length using an O(1) auxiliary space.
def insert(l,k):
    i=0
    j=0
    m=[]
    count=0
    while i<len(l):
        if l[i]!=k:
            i+=1
        else:
            l.pop()
            count+=1
            i+=1
    while j<len(l):
        if l[j]==k:
            m.append(k)
            m.append(k)
            j+=1
        else:
            m.append(l[j])
            j+=1
    return m
print(insert([1, 0, 2, 3,0,4,5,67,8],0))
    