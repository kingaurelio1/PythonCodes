def findTheDifference(s,t):
    hashmap={}
    for i in range(len(s)):
        if s[i] in hashmap:
            hashmap[s[i]]+=1
        else:
            hashmap[s[i]]=1
    for j in range(len(t)):
        if t[j] not in hashmap:
            return t[j]
        else:
            hashmap[t[j]]-=1
            if hashmap[t[j]] < 0:
                return t[j]