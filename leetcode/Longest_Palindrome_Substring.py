s="babad"
s="ccc"
s="ccd"

ans=[]

def expand(left:int, right:int)->str:
    while left>=0 and right<=len(s) and s[left]==s[right-1]:
        left-=1
        right+=1
    return s[left+1:right-1]
if len(s)<2 or s==s[::-1]:
    ans=s
for i in range(len(s)-1):
    print(i, expand(i, i+1), expand(i, i+2))
    ans=max(ans, expand(i, i+1), expand(i, i+2), key=len)
    print("ans:", ans)
print(ans)
