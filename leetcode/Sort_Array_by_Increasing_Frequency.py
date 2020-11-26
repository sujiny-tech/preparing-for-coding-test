import collections

nums=[2,3,1,3,2]
#[1,1,2,2,2,3]

def frequencySort(nums):
    #counting...
    cnt=collections.defaultdict(int)
    for i in range(len(nums)):
        cnt[nums[i]]+=1
    
    #same -> cnt=collections.Counter(nums)

    nums=sorted(nums, reverse=True) ##
    nums=sorted(nums, key=lambda x : cnt[x])

    return nums


print(frequencySort(nums))
