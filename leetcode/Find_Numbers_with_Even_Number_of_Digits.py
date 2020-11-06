nums=[12, 345, 2, 6, 7896]
def findNumbers(nums):
    #solution 1

    #list_num=[len(str(x)) for x in nums]
    #cnt=[x%2==0 for x in list_num]
    #return cnt.count(True)
    
    #solution 2
    cnt=0
    list_=list(map(str, nums))
    for num in list_:
        if len(num)%2==0:
            cnt+=1
    return cnt

print(findNumbers(nums))
