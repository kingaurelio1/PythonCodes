#Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#You can use each character in text at most once. Return the maximum number of instances that can be formed.

def balloon(t):
    d={}
    s=0
    for n in "balon":
        d[n]=0
    for i in t:
        d[i]=0
    for i in t:
        d[i]+=1
    m=min(d["b"],d["a"],d["n"])
    d["b"],d["a"],d["n"]=m,m,m
    d["l"],d["o"]=min(d["l"],d["o"]),min(d["l"],d["o"])
    for k in "balon":
        s+=d[k]
    return s//7
print(balloon("ballonnnn")) 