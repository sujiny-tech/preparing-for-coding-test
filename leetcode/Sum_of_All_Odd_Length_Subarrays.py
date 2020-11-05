arr=[1,4,2,5,3] #[10,11,12]

def sumOddLengthSubarray(arr):
    ans=0
    iter_num=(len(arr)+1)//2
    for i in range(iter_num):
        for j in range(len(arr)-(2*i)):
            ans+=sum(arr[j:j+(2*i)+1])
        
    return ans


print(sumOddLengthSubarray(arr))
