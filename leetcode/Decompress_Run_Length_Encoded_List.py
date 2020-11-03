nums=[1, 1, 2, 3]

def decompressRLElist(nums):
    array=[]
    for i in range(0, len(nums), 2):
        array+=[nums[i+1]]*nums[i]
        
    return array

print(decompressRLElist(nums))
