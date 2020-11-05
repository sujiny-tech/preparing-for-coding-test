s="RLRRLLRLRL"

def balancedStringSplit(s):
    ans=0
    l_cnt,r_cnt=0,0
    s=list(s)
    while s:
        s_=s.pop(0)
        if s_=='R':
           r_cnt+=1
        if s_=='L':
           l_cnt+=1
        if r_cnt==l_cnt:
           ans+=1
           l_cnt=0
           r_cnt=0
                
    return ans

print(balancedStringSplit(s))
