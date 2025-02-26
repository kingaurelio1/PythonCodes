#Función que elimina espacios de un string
def eliminateSpaces(s):
    left=0
    right=1
    t=''
    if len(s)==0:
        return s
    while right<len(s):
        if s[left]!=' ' and right<len(s)-1:
            t+=s[left]
            left+=1
            right+=1
        elif s[left]!=' ' and right==len(s)-1:  
            t+=s[left]
            left+=1
            right+=1
        else:
            left+=1
            right+=1
    if s[left]!=' ':
        t+=s[left]

    return t
print(eliminateSpaces('            1'))

def eliminatespaces1(s):
    t=''
    if len(s)==0:
        return s
    else:
        for i in range(len(s)):
            if s[i]!=' ':
                t+=s[i]
        return t
print(eliminatespaces1('123   4'))

