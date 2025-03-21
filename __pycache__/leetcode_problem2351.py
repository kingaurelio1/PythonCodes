#Given a string s consisting of lowercase English letters, return the first letter to appear twice.

def repeatedCharacter(s):
    hashset=set()
    for i in range(len(s)):
        if s[i] in hashset:
            return s[i]
        else:
            hashset.add(s[i])
print(repeatedCharacter('abccdefg'))