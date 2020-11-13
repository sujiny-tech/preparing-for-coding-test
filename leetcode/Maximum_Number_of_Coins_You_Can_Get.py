import itertools

piles=[2,4,1,2,7,8]

def maxCoins(piles):
    #sorting
    piles=sorted(piles, reverse=True)
    l=len(piles)
    
    #num of choices
    cnt=l//3
    ans=0

    for i in range(cnt):
        print(piles[(2*i)+1])
        ans+=piles[(2*i)+1]
    return ans


print(maxCoins(piles))
