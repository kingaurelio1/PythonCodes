alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def alphabet_index(alphabet, string):
    i=len(alphabet)-1
    s=""
    while i>-1:
        if alphabet[i] in string.lower():
            s= str(i+1) + alphabet[i]
            break
        else:
            i-=1
            continue 
    return s