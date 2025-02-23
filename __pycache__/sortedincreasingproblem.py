#Crear una función que te de la longitud del subarray más grande de un array.
def increasingSubarray(l):
    sum=1
    max=0
    left=0
    right=1
    if len(l)==0:
        return 0
    elif len(l)==1:
        return 1
    else:
        while right<len(l):
            if l[left]< l[right]:
                sum+=1
                left=right
                right+=1
                if max<sum:
                    max=sum
            else:
                if max<sum:
                    max=sum
                sum=1
                left=right
                right+=1

        return max
print(increasingSubarray([-1,-3,-4,4]))