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