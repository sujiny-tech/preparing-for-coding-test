num=9669

def maximum69Number(num):
    s=list(str(num))
    results=''
    while s:
        s1=s.pop(0)
        if s1=='6':
            s1='9'
            results+=s1
            break
        results+=s1
    return results+''.join(s)

print(maximum69Number(num))