#Definir una función que te regrese la sucesion máximo de 0 y 1 consecutivos.
def maximum(l):
    sum=1
    left=0
    right=1
    max1=0
    while right<len(l):
        print(left,right,sum,max)
        if l[left] == l[right]:
            sum+=1
            right+=1
        else:
            if sum > max1:
                max1=sum
            left=right
            right+=1
            sum=1
    return max(sum, max1)
print(maximum([0, 0, 0,0]))