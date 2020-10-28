import itertools

nums=[3,30,34, 5,9]
#[10,2]
#
def largesNumber(nums):
    if len(nums)==1:
        return str(nums)
#    a="34"
#    print(a, a[0], a[1])

    nums=list(map(str, nums))
#    print("str:", nums)
    for i in nums:
        print(i[0])

    nums=sorted(nums, key=lambda x:x[0], reverse=True)
    print("sorted:", nums)
    return

print(largesNumber(nums))
