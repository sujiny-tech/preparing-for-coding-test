n=10
start=5

def xorOperation(n, start):
    ans=0
    for i in range(n):
        ans=ans^(start+2*i)
    return ans

print(xorOperation(n, start))