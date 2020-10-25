import re
s="A man, a plan, a canal: Panama"
#s="race a car"
result=""
ans=True
for c in s:
    if c.isalnum():
        c=c.lower()
        result+=c
'''
cnt=0

for i in range(len(s)):
    if s[i]==s[-(i+1)]:
        cnt+=1

    if cnt>=4:
        ans=True
'''
mid=(len(result)//2)
#print(mid) #0~20
if len(result)>1:
    for i in range((len(result)//2)):
        if result[i]!=result[-(i+1)]:
            ans=False

s1=s.lower()
s1=re.sub('[^a-z0-9]', '', s1)
print(s1)
print(s1[::-1])

#print(result)
print(ans)