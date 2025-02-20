def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1


    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):
        
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest
