#나는 내 아이들에게 쿠키를 나눠줄예정
#적어도 쿠키 하나씩 나눠줘야한다.
#각 아이 i는 gi(greed factor)을 갖는다
#gi : 아이가 만족하는 쿠키의 최소 사이즈.
#sj : 쿠키 j의 크기
#if sj>=gi, 아이i에게 쿠키 j를 배정할수있음.
#Goal - to maximiae the number of your content children and output the maximum number.
#최대한 아이들이 만족할수있는 아이들은 몇명?
g=[1,2,3]
s=[1,1]
#1번 아이는 최소 1이어야 만족, 1번쿠키 해당
#2번 아이는 최소 2어야 만족, 1,2번 쿠키 해당
#3번 아이는 최소 3이어야 만족, 1,2번 먹어도 소용 x
#g=[1,5,7]#[1,2]
#s=[1,2,3]
#1 : 최소 1, 1번 쿠키 해당
#2 : 최소 2, 2번 쿠키 해당
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
