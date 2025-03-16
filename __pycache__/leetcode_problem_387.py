#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#Primera idea
def FirstUnique(s):
    hashmap={}
    for i in range(len(s)):
        if s[i] in hashmap:
            hashmap[s[i]]=s[i]
        else:
            hashmap[s[i]]=i
    for j in hashmap.keys():
        if hashmap[j]!=j:
            return hashmap[j]
    return -1
print(FirstUnique("dddccdbba"))