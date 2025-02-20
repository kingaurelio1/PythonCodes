#Crear una función que me de el tercer elemento más grande

def thirlargest(l):
    if len(l) < 3:
        return -1
    else:
        max1=-1
        max2=-1
        max3=-1
        for i in range(len(l)):
            if l[i]>max1:
                max1=l[i]
        for j in range(len(l)):
            if l[j] > max2 and l[j]!=max1:
                max2=l[j]
        for k in range(len(l)):
            if l[k] > max3 and l[k]!=max1 and l[k]!=max2:
                max3=l[k]
        return max3
print(thirlargest([1,2,4,5,78,9,9,0,4]))