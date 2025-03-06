#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

def MergeStr(s1,s2):
    pointer1=0
    s=""
    if len(s1)< len(s2):
        while pointer1<len(s1):
            s+=s1[pointer1]+s2[pointer1]
            pointer1+=1
        s+=s2[pointer1::]
    elif len(s1) > len(s2):
        while pointer1<len(s2):
            s+=s1[pointer1]+s2[pointer1]
            pointer1+=1
        s+=s1[pointer1::]
    else:
        while pointer1<len(s1):
            s+=s1[pointer1]+s2[pointer1]
            pointer1+=1
    return s
print(MergeStr("abcd","pq"))