#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def commonPrefix(a):
    if not a:
        return "" # Return nothing if input is empty

    s = ""

    for i in range(len(a[0])):  
        for w in a:
            if len(w) <= i or a[0][i] != w[i]:  
                return s  # Stop on first mismatch
        s += a[0][i]

    return s



print(commonPrefix(["flower","flow","flight"]))