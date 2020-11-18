n=6

def minOperations(n):
    arr=[(2*x)+1 for x in range(n)]

    target=sum(arr)//n

    cnt=0
    for i in range(n//2):
        if arr[i]<target:
            cnt+=target-arr[i]
            arr[i]=target
            arr[-(i+1)]=target
    
    return cnt

print(minOperations(n))
