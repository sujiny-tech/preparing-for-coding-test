s="Hello"

def toLowerCase(s):
    #solution 2
    s=list(s)
    for i in range(len(s)):
        if s[i].upper():
            s[i]=s[i].lower()
    return ''.join(s)

    #solution 1
    #return s.lower()

print(toLowerCase(s))
