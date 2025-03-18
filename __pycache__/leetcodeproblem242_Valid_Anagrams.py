#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def ValidAnagram(s,t):
    if len(s)!=len(t):
        return False
    hashmap={}
    for i in range(len(s)):
        if s[i] in hashmap:
            hashmap[s[i]]+=1
        else:
            hashmap[s[i]]=1
    for j in range(len(t)):
        if t[j] in hashmap and hashmap[t[j]] >=0 :
            hashmap[t[j]]-=1
        else:
            return False
    for k in range(len(s)):
            if hashmap[k]!=0:
                return False
    return True
x = "rat"
y = "car"
print(ValidAnagram(x,y))
