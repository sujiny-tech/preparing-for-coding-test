#nums = [2, 7, 11, 15]
#target = 9
nums=[3,3]
target=6
'''
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            print(i, j)
            break
'''
for i in range(len(nums)):
    if target-nums[i] in nums[i+1:]:
        print(i, nums[i+1:].index(target-nums[i])+(i+1))
        break
#print(0,0)
