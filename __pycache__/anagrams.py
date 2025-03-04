#Given two strings s1 and s2 consisting of lowercase characters, the task is to check whether the two given strings are anagrams of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different.
def anagrams(s1,s2):
    d1={}
    d2={}
    if len(s1)!=len(s2):
        return False
    else:
        for i in range(len(s1)):
            d1[s1[i]], d2[s1[i]],d2[s2[i]]=0,0,0
        for j in range(len(s1)):
            d1[s1[j]]+=1
            d2[s2[j]]+=1
        for key in d2.keys():
            if d1[key]!=d2[key]:
                return False,d1,d2
        return True
print(anagrams("eat","car"))