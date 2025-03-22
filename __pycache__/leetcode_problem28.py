#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Primera idea
def strStr(haystack, needle):
    sum1=''
    for i in range(len(haystack)):
        sum1+=haystack[i]
        if len(sum1)==len(needle):
            if sum1==needle:
                return i-len(needle)+1
            else:
                sum1=sum1[i-len(needle)+2::]
    return -1,sum1

#idea 2
def strStr2(haystack, needle): 
        sum1=''
        n=len(haystack)
        m=len(needle)
        l,r=0,0
        index=0
        if n==1 and m==1:
            if needle==haystack:
                return 0
            else:
                return -1
        while r < n:
            if l < m:
                if needle[l]==haystack[r]:
                    l+=1
                    r+=1
                else:
                    l=0
                    r+=1
                    index=r
            else:
                return index
        if l==m:
            return index
        else:
            return -1
        
#Mi solución:
def strStr3(haystack, needle):
        sum1=''
        n=len(haystack)
        m=len(needle)
        index=0
        hashmap={}
        for i in range(len(haystack)):
            sum1+=haystack[i]
            if len(sum1)==m:
                if needle in hashmap:
                    return hashmap[needle]
                else:
                    hashmap[sum1]=index
                    index+=1
                    sum1=sum1[1::]
        if needle in hashmap:
            return hashmap[needle]
        else:
            return -1