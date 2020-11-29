nums=[4,2,5,7]#[4,1,1,0,1,0]

def sortArrayByParity(nums):
    '''
    #solution 2.
    nums=sorted(nums, key=lambda x:x%2!=0)
    mid=len(nums)//2
    for i in range(mid):
        nums.insert((2*i+1), nums.pop(mid+i))
    return nums
    '''
    #solution 1.
    even=[]
    odd=[]
    
    for i in range(len(nums)):
        if nums[i]%2==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    i=1
    while odd:
        odd_num=odd.pop(0)
        even.insert(i, odd_num)
        i+=2
    return even

print(sortArrayByParity(nums))