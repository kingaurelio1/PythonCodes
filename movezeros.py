#Una función que me mueva los zeros.
def movezero(l1):
    l2=[]
    count=0
    for i in range(len(l1)):
        if l1[i]==0:
            count += 1
        else:
            l2.append(l1[i])
    for j in range(count):
        l2.append(0)
    return l2
print(movezero([0,0,0,0,1,3,12]))
