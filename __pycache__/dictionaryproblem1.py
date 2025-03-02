#Given a string str, the task is to find the frequency of each character of a string using a disctionary

def countletter(s):
    d={}
    for i in range(len(s)):
        d[s[i]]=0
    for n in range(len(s)):
        d[s[n]]+=1
    return d
print(countletter("geeksforgeeks" ))