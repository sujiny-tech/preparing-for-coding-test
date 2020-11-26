s="IDID"

def diStringMatch(s):
    arr=[x for x in range(len(s)+1)]
    ans=[]

    for i in range(len(s)):
        if s[i]=='I':
            ans.append(arr.pop(0))
        else:
            ans.append(arr.pop())
    
    return ans+arr

print(diStringMatch(s))
