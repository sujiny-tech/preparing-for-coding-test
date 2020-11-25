A = ["cba","daf","ghi"]

def minDeletionSize(A):
    ans=0
    n=len(A[0])
    for i in range(n):
        mid=[]
        for a in A:
            mid.append(a[i])
        if mid!=sorted(mid):
            ans+=1
    
    return ans


print(minDeletionSize(A))
