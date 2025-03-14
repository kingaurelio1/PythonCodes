#Given a string s, find the length of the longest substring without duplicate characters.
 
def Longest(s):
    hashset=set()
    l,r=0,1
    max1=0
    hashset.add(s[l])
    while r < len(s):
        if s[r] not in hashset:
            hashset.add(s[r])
            r+=1
        else:
            if len(hashset)> max1:
                max1=len(hashset)
            hashset.clear()
            l+=1
            r=l+1
            hashset.add(s[l])
    return max(max1,len(hashset))
print(Longest("abcdefghijklmnopqrstuvwxyz"))