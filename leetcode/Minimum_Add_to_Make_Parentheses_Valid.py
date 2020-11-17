S=")()"

def minAddtToMakeValid(S):
    stack=[]
    no_=0
    yes_=0
    S=list(S)
    while S:
        s=S.pop(0)
        if s=="(":
            stack.append(s)
        else:
            if len(stack)==0:
                no_+=1
            else:
                stack.pop()
                yes_+=2

    return no_+len(stack)

print(minAddtToMakeValid(S))