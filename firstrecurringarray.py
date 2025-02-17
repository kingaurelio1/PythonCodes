#Crear una función que te de el elemento que se repita en una lista.
def firstrecurringarray(l):
    t='Undefined'
    r=0
    left=0
    right=1
    m=len(l)
    while left < m:
        if left ==m-1:
            return t 
        elif l[left] != l[right] and right == m-1:
            left += 1
            right= left + 1
        elif l[left] != l[right] and right < m-1:
            right+=1
        else:
            r=l[left]
            return r
print(firstrecurringarray([1,3,4,5,6,7,3,2]))