import itertools
n = 4
k = 2

nums=[i for i in range(1, n+1)]

a=list(itertools.combinations(nums, k))
print(a)

def combine(n, k):
    nums=[i for i in range(1, n+1)]
    result=[]
    def dfs(elements, start, k):
        if k==0:
            result.append(elements[:])

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], 1, k)
    return result

print(combine(n, k))
