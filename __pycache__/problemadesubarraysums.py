#Given an array of n positive integers, your task is to count the number of subarrays having sum x.

def sumarray(l,x):
    left=0
    right=1
    count=0
    sumleft=0
    sumright=0
    while right < len(l):
        if left>len(l)-1:
            break

        sumleft+=l[left]
        sumright+=l[right]
        if sumleft < x and sumright<x:
            left+=1
            right+=1
        elif sumright==x and sumleft<x:
            sumright=0
            count+=1
            left+=1
        elif sumleft==x and sumright<x:
            sumleft=0
            count+=1
            left+=1
            right+=1
        elif sumleft==x and sumright==x:
            sumleft=0
            sumright=0
            count+=2
        elif sumleft< x and sumright>x:
            sumright=0
            left+=1
        elif sumright==x and sumleft>x:
            sumright=0
            count+=1
            sumleft=0
            left+=1
            right+=1
        elif sumleft==x and sumright>x:
            sumleft=0
            sumright=0
            count+=1
            right+=1

        #print(sumleft,sumright)
        print(count,left,right,sumleft,sumright)
    return count

print(sumarray([2,4,1,2,4],7))

