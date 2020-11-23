prices=[8,4,6,2,3]

def finalPrices(prices):
    ans=[]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i]>=prices[j]:
                ans.append(prices[i]-prices[j])
                break
            else:
                if j==len(prices)-1:
                    ans.append(prices[i])
                    break
                else:
                    continue
    ans.append(prices[-1])

    return ans

print(finalPrices(prices))
