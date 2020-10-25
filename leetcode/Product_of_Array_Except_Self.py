nums=[1,2,3,4]
#nums=[0,0]
#nums=[1,0]
#nums=[1,1,2,3]
#nums=[-1,-1]
#[6, 6, 3, 2]
#given an array nums of n integers where n>1,
#return an array output
#such that output[i] is equal to the product of all the elements of nums except nums[i]
#각 인덱스에 해당하는 값을 빼고 나머지 값들의 곱을 계산한다.
ans=[]
right=[]
mid=1
#for loop 2-> time limit
#나눗셈 사용 X -> 곱셈 사용하라는 뜻
#[1,1,2,6]
ans.append(mid)
for i in range(len(nums)-1):
    mid*=nums[i]
    ans.append(mid)
print(ans)
mid=1
#[1,1,2,6]
#[24, 12, 4, 1]
#[24, 12, 8, 6]
for i in range(len(nums)-1, -1, -1):
    ans[i]*=mid
    mid*=nums[i]
print(mid)
print(ans)

'''
for i in range(len(nums)):
    if i==0:
        for j in range(i+1, len(nums)):
            mid=mid*nums[j]
        ans.append(mid)
        print(ans)
    else:
        if ans[0]==0:
            ans.append(0)
        else:
            ans.append(int(ans[0]/nums[i])*nums[0])
print(ans)
'''
'''
for i in range(len(nums)):
    mid=1
    for j in range(len(nums)):
        if i==j or nums[j]==1:
            continue
        else:
            mid=mid*nums[j]
    ans.append(mid)
print(ans)
'''