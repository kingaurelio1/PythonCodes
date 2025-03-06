#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(a,w):
    pointer1=0
    pointer2=0
    count=0
    if len(a)>len(w):
        return False
    else:
        while pointer2<len(w):
            if pointer1<len(a):
                if a[pointer1]==w[pointer2]:
                    count+=1
                    pointer1+=1
                    pointer2+=1
                else:
                    pointer2+=1
            else:
                break
        return count==len(a)
print(isSubsequence("abc","ahcgdb"))