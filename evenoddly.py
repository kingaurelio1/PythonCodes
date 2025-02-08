def char_at_pos(r, s):
    t = []
    w = ""
    
    if s == "even":
        if type(r) is list:
            for i in range(1, len(r), 2):
                t.append(r[i])
        else:
            for i in range(0, len(r), 2):
                w += r[i]
    elif s == "odd":
        if type(r) is list:
            for i in range(1, len(r), 2):
                t.append(r[i])
        else:
            for i in range(1, len(r), 2):
                w += r[i]
    else:
        return "Error"
    
    if type(r) is list:
        return t
    else:
        return w
print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(type("str"))