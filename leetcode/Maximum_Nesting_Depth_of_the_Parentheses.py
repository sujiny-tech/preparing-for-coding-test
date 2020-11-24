#s="1+(2*3)/(2-1)"
s="(1)+((2))+(((3)))"
#s="(1+(2*3)+((8)/4))+1"

def maxDepth(s):
    cnt=0
    depth=0
    for s1 in s:
        if s1=="(":
            cnt+=1
        elif s1==")":
            cnt-=1
        else:
            continue
        depth=max(cnt, depth)
    return depth


print(maxDepth(s))
