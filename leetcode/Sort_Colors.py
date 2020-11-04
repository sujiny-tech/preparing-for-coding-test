nums=[2,0,2,1,1,0]

def sortColors(nums):
    #without using the library's sort funtion
    #one-pass algorithm using only O(1) constant space

    #Dutch National Flag Problem
    r, w, b=0, 0, len(nums)

    while w<b:
        if nums[w]<1:
            nums[w], nums[r]=nums[r], nums[w]
            w+=1
            r+=1
        elif nums[w]>1:
            b-=1
            nums[w], nums[b]=nums[b], nums[w]
        else:
            w+=1

    return nums


print(sortColors(nums))
