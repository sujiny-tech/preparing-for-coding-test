import collections

nums=[2,2,3,1,1,1]
k=2

def topKFrequent(nums, k):
    #first solution
    answer=[]
    cnt=collections.Counter(nums)
    for num, cnt in cnt.most_common(k):
        answer.append(num)
    return answer

    #second solution
    #return list(zip(*collections.Counter(nums).most_common(k)))[0]

print(topKFrequent(nums, k))