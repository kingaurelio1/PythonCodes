#Coins problem
#primera idea
def Coins(a,s):
    l=len(a)-1
    current,m,i=0,l,l
    while i >-2:
        print(current,s)
        if s>0:
            current+=s//a[i]
            s-=a[i]*(s//a[i])
            i-=1
        else:
            break
    return current if s==0 else -1
print(Coins([186,419,83,408],6249))