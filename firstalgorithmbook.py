#Vamos a escribir un código que recibe como input una lista y un target. El output regresa el índice si lo encuentra y si no regres null
def funct(array,target):
    s=None
    i=0
    while i < len(array):
        if array[i]==target:
            s=i
            break
        else:
            i+=1
            continue
    return s
print(funct([1,2,3,4,5,6,7,8],10))