nums=[3, 30, 34, 5, 9]
#[432, 43243]
#[1]
#[10,2]

def to_swap(n1, n2):
    return str(n1)+str(n2)<str(n2)+str(n1)
    
def largestNumber(nums):
    #another solution
    i=1
    while i<len(nums):
        j=i
        while j>0 and to_swap(nums[j-1], nums[j]):
            nums[j], nums[j-1]=nums[j-1], nums[j]
            j-=1
        i+=1

    return str(int(''.join(map(str, nums))))

    ##solution 1
    #if len(set(nums))==1 and nums[0]=='0':
    #    return '0'
    #if len(nums)==1:
    #    return str(nums)

    #nums.sort(reverse=True)
    #nums=list(map(str, nums))
    
    ##constraints : 0<=nums[i]<=10^9 -->max_num_length=9
    #nums_=[(nums[i]*(9))[:9] for i in range(len(nums))]
    #ans=''

    #for i in range(len(nums)):
    #    ind=nums_.index(max(nums_))
    #    nums_[ind]='0'
    #    ans+=nums[ind]

    #return ans


print(largestNumber(nums))
