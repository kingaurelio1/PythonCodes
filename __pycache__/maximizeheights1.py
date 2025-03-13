#Given the heights of n towers and a positive integer k, increase or decrease the height of all towers by k (only once). After modifications, the task is to find the minimum difference between the heights of the tallest and the shortest tower.

#primera idea
def heights(a,k):
    min=0
    max=0
    for i in range(len(a)):
