#https://leetcode.com/problems/palindrome-number/description/
#Conviertiendo el número a un string
def palindrome(n):
    t=True
    if n<0:
        return False
    elif 0<=n<10:
        return True
    else:
        s=str(n)
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                t=False
                break
            else:
                left+=1
                right-=1
                continue
        return t
print(palindrome(-121))
#

def isPalindrome(n):
    if n < 0:
        return False

    reverse = 0
    xcopy = n

    while n > 0:
        reverse = (reverse * 10) + (n % 10)
        n //= 10
        
    return reverse == xcopy
print(isPalindrome(121012002))