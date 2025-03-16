#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

#There is only one repeated number in nums, return this repeated number.

def FMN(a):
    numbers=set()
    for i in range(len(a)):
        if a[i] in numbers:
            return a[i]
        else:
            numbers.add(a[i])
    