nums=[1,5,4,5]

def maxProduct(nums):
    #solution 1. sorting
    nums=sorted(nums, reverse=True)

    return (nums[0]-1)*(nums[1]-1)

    #solution 2. brute force
    #all_=[]
    #for i in range(len(nums)-1):
    #    for j in range(i+1, len(nums)):
    #        all_.append((nums[i]-1)*(nums[j]-1))
    #return max(all_)
        
print(maxProduct(nums))

