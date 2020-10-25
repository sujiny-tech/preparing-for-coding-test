s=["h","e","l","l","o"]
result=""
'''
for c in s:
    result+=c
result=result[::-1]

for i in range(len(s)):
    s[i]=result[i]
'''
mid=len(s)//2
for i in range(mid):
    tmp=s[i]
    s[i]=s[-(i+1)]
    s[-(i + 1)]=tmp
print(s)