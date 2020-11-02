nums=[2,5,1,3,4,7]
n=3

def shuffle(nums, n):
    answer=[]

    for i in range(n):
        answer.append(nums[i])
        answer.append(nums[n+i])
    return answer

print(shuffle(nums, n))
