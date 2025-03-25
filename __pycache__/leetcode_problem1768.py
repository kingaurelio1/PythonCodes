#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        sum1=''
        if len(word1) < len(word2):
            while i<len(word2):
                if i >=len(word1):
                    sum1+=word2[i]
                    i+=1
                else:
                    sum1+=word1[i]+word2[i]
                    i+=1
        else:
            while i<len(word1):
                if i >=len(word2):
                    sum1+=word1[i]
                    i+=1
                else:
                    sum1+=word1[i]+word2[i]
                    i+=1
        return sum1