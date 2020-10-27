import collections
import itertools
nums=[1,2,3,1,1,3]

def numIdenticalPairs(nums):
    ans=0
    pairs=collections.defaultdict(list)
    for i in range(len(nums)):
        pairs[nums[i]].append(i)
    for pair in pairs.values():
        if len(pair)<=1:
            continue
        else:
            ans+=len(list(itertools.combinations(pair, 2)))
    return ans

print(numIdenticalPairs(nums))