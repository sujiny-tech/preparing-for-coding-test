s="aiohn"
indices=[3,1,4,2,0]

def restoreString(s, indices):
    lst_s=['']*len(s)
    s=list(s)

    while indices:
        num=indices.pop()
        s_=s.pop()
        lst_s[num]=s_
    return ''.join(lst_s)

print(restoreString(s, indices))
