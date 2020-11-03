import collections

nums=[8,1,2,2,3]

def smallerNumbersThanCurrent(nums):

    arr=[]
    num_sort=sorted(nums)
    table=collections.defaultdict(int)
    for i in range(len(num_sort)):
        if num_sort[i] in table:
            continue
        else:
            table[num_sort[i]]=i

    for i in range(len(nums)):
        arr.append(table[nums[i]])
    return arr    

'''
    #solution 2
    arr=[]
    for num in nums:
        arr.append([i<num for i in nums].count(True))
    return arr
''' 

'''
    #solution 1
    arr=[]
    for i in range(len(nums)):
        cnt=0
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                cnt+=1
        arr.append(cnt)
    return arr
'''

print(smallerNumbersThanCurrent(nums))
