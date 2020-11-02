nums=[1,2,3,4]

def runningSum(nums):
    
    for i in range(1, len(nums)):
        nums[i]=nums[i-1]+nums[i]

    return nums

    #solution 2
    #return [sum(nums[:i+1]) for i in range(len(nums))]
    

print(runningSum(nums))
