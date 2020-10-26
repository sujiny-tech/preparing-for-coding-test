nums=[1,2,3,4]

#given an array nums of n integers where n>1,
#return an array output
#such that output[i] is equal to the product of all the elements of nums except nums[i]

ans=[]
right=[]
mid=1

ans.append(mid)
for i in range(len(nums)-1):
    mid*=nums[i]
    ans.append(mid)
print(ans)
mid=1

for i in range(len(nums)-1, -1, -1):
    ans[i]*=mid
    mid*=nums[i]
print(mid)
print(ans)
