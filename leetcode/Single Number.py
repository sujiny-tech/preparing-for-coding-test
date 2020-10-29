import collections

nums=[3,3,1]

def singleNumber(nums):

    #solution 1
    ans=0
    for num in nums:
        ans=ans^num
        
    return ans
    '''
    #solution 3
    cnt=collections.Counter(nums)
    for num, val in cnt.items():
        if val==1:
            return num
    '''

    '''
    #solution 2
    set_num=list(set(nums))
    for num in set_num:
        if nums.count(num)==1:
            return num
    '''

print(singleNumber(nums))
