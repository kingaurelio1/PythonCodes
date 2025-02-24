#Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

def stocks(a):
    left=0
    right=1
    max=0
    sum=0
    while right < len(a):
        if a[left] >= a[right]:
            left=right
            right+=1
        else:
            sum = a[right]-a[left]
            if sum > max:
                max=sum
            right+=1
    return max
print(stocks([7,1,5,3,6,4]))
