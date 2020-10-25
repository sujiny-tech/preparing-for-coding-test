import collections

numCourese=3
#prerequisites=[[1,0]]
prerequisites=[[0,1], [0,2], [1,2]]#[[1,0], [0,2], [1,2]]
#순환구조인지 아닌지 판별하는 것.

q=collections.defaultdict(list)
for a,b in prerequisites:
    q[a].append(b)
    #q[a].append(a)
print(q)

def canFinish(numCourese, q):
    s=[]
    check=True
    def dfs(num):
        c=True
        print(num, s)
        if num in s:
            c=False
            print("순환!!", c)
            return c
        else:
            s.append(num)
            for i in q[num]:
                if dfs(i)==False:
                    c=False
                    break
            return c

    for i in range(numCourese):
        s=[]
        if check:
            check=dfs(i)
        else:
            break
    print(check)

print(canFinish(numCourese, q))

