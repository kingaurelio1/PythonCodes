#Given an integer array arr[] and an integer ele the task is to the remove all occurrences of ele from arr[] in-place and return the number of elements which are not equal to ele. If there are k number of elements which are not equal to ele then the input array arr[] should be modified such that the first k elements should contain the elements which are not equal to ele and then the remaining elements.

def ocuur(a,n):
    sum=0
    for i in range(len(a)):
        if a[i]!=n:
            sum+=1
    return sum
print(ocuur([2,2,1,2,4,2],2))