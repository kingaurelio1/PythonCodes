#Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

def Unique(a):
    hashmap={}
    hashset=set()
    for i in range(len(a)):
        if a[i] in hashmap:
            hashmap[a[i]] +=1
        else:
            hashmap[a[i]]=1
    for key in hashmap.keys():
        if hashmap[key] in hashset:
            return False
        else:
            hashset.add(hashmap[key])
    return True
print(Unique([1,2,2,1,]))