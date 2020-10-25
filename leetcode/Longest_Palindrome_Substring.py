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
'''
#input="babad"
input="babbd"
input="cbbd"
input="ccc"
input="ccd"
#input="bb"
#문자열 s 주어지면, 가장 긴 팰린드롬 찾아라. 최대 1000
#중간값에서부터 탐색해서 비교하는 방법
mid=int((len(input)/2)+0.5)
#print(mid)
ans=[]
if len(input)<2 or input==input[::-1]:
    m_ans=input
elif len(input)%2!=0:
    i=1
    #여기서 mid 전과후만 비교하므로, 여기서 에러나는 거임.(잘못 구현함)
    mid = int((len(input) / 2) + 0.5)
    print(mid)
    m_ans=input[mid-1]
    while mid!=0:
        if mid-1+i>=len(input):
            break
        #print(mid-i, mid+i, input[mid-i], input[mid+i])
        if input[mid-1-i]==input[mid-1+i]:
            if len(m_ans)<len(input[mid-1-i:mid-1+i+1]):
                m_ans=input[mid-1 - i:mid-1 + i+1]
                #print(m_ans)
            i += 1
        else:
            mid-=1
            i=1
            print("mid 변경:",mid)
    print(m_ans)
else:
    i=1
    mid=int((len(input) / 2) + 0.5)
    #print(mid)
    m_ans=input[mid-1]
    while mid!=0:
        if mid-1+i>=len(input):
            break
        #print(mid-i, mid+i, input[mid-i], input[mid+i])
        if input[mid-1]==input[mid-1+i]:
            #print(mid-1+i+1, input[mid-1:mid-1+i+1])
            if len(m_ans)<len(input[mid-1:mid-1+i+1]):
                m_ans=input[mid-1:mid-1+i+1]
                #print(m_ans)
            i += 1
        else:
            mid-=1
            i=1
            print("mid 업")
    print(m_ans)
'''
