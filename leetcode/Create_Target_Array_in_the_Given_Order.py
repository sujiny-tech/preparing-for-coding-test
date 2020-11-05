nums=[0,1,2,3,4]
index=[0,1,2,2,1]

def createTargetArray(nums, index):
    target=[]
    for n, i in zip(nums, index):
        target.insert(i,n)
    return target


print(createTargetArray(nums, index))
