nums=[4,6,5,9,3,7]
l=[0,0,2]
r=[2,3,5]

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]

def check(arr):
    diff=200000
    for i in range(1, len(arr)):
        if diff==200000:
            diff=arr[i]-arr[i-1]
        else:
            if diff==arr[i]-arr[i-1]:
                continue
            else:
                return False
    return True

def checkArithmeticSubarrays(nums, l, r):
    answer=[]
    for l1, r1 in zip(l, r):
        A=sorted(nums[l1:r1+1])
        answer.append(check(A))
    return answer

print(checkArithmeticSubarrays(nums, l, r))