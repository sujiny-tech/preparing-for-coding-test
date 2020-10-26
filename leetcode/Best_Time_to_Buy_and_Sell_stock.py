import sys

prices=[7,1,5,3,6,4]
#prices=[2,4,1]
#prices=[7,6,5,4,3,1]
#Say you have an array for which the i-th element is the price of a given stock on day i.
#if you were only permiitted to complete at most one transaction,
#design an algorithm to find th maximunm profit.
ans=0
min_val=sys.maxsize
for price in prices:
    min_val=min(min_val, price)
    ans=max(price-min_val, ans)
print(ans)

#time limit
'''
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        ans=max(prices[j]-prices[i], ans)
print(ans)
'''
