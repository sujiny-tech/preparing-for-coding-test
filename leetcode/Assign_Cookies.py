#Goal - to maximiae the number of your content children and output the maximum number.
g=[1,2,3]
s=[1,1]
cnt=0

g=[10,9,8,7]
s=[5,6,7,8]
g.sort()
s.sort()
#7,8,9,10
#5,6,7,8
child_i=cookie_j=0
while child_i<len(g) and cookie_j<len(s):
    if g[child_i]<=s[cookie_j]:
        child_i+=1
    cookie_j+=1
print(child_i)

'''
g.sort()
s.sort()
for i in range(len(g)):
    sum=0
    for j in range(len(s)):
        if g[i]<=s[j]:
            cnt+=1
            s.pop(j)
            break
'''


print(cnt)
