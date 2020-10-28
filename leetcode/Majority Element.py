import math
import collections
nums=[3,2,3]

def majorityElement(nums):
    #solution 5)
    return sorted(nums)[len(nums)//2]    

    #solution 4)
    #if not nums:
    #    return None
    #if len(nums)==1:
    #    return nums[0]
    #mid=len(nums)//2
    #a=self.majorityElement(nums[:mid])
    #b=self.majorityELement(nums[mid:])
    #return [b, a][nums.count(a)>mid]
    
    #solution 3) dynamic programming
    #counts=collections.defaultdict(int)
    #for num in nums:
    #    if counts[num]==0:
    #        counts[num]=nums.count(num)
    #    if counts[num]>len(nums)//2:
    #        return num
    
    #solution 2)
    #num_set=list(set(nums))
    #for num in num_set:
    #    if nums.count(num)>len(nums)//2:
    #        return num

    #solution 1)
    #return collections.Counter(nums).most_common(1)[0][0]

print(majorityElement(nums))
