#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

def searchlist(a,b):
    middle=len(a)//2
    if len(a)==2:
        if 
    if b>middle:
        return searchlist(a[middle+1::],b)
    elif b<middle:
        return searchlist(a[::middle],b)
print(searchlist([1,3,4,5],5))