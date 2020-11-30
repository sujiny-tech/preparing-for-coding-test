s="abbaca"

def removeDuplicates(s):
    #solution 2.
    stack=[]
    i=0
    while i<len(s):
        if len(stack)!=0 and stack[-1]==s[i]:
            i+=1
            stack.pop(-1)
        else:
            stack.append(s[i])
            i+=1
    return ''.join(stack)

    '''
    #solution 1.
    s=list(s)
    while s:
        check=False
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s.pop(i)
                s.pop(i)
                check=True
                break
        if check==False:
            break

    return ''.join(s)
    '''

print(removeDuplicates(s))