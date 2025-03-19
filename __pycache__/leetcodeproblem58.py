#Given a string s consisting of words and spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.

def safe(s):
    currentsum=''
    r=len(s)-1
    while r>-1:
        if s[r]==' ' and len(currentsum) >0:
            return len(currentsum)
        elif s[r]==' ' and len(currentsum)==0:
            r-=1
        else:
            currentsum+=s[r]
            r-=1
    return len(currentsum)
print(safe('Today is a nice day'))