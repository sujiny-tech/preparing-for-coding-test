input=[7,1,5,3,6,4]
input=[]
#input=[1,2,3,4,5]
#input=[7,6,4,3,1]

if len(input)==0:
    profit=0
else:
    min_val = max(input)  # sys.maxsize
    profit = 0
    for i in range(len(input)):
        min_val=min(input[i], min_val)
        profit=max(profit, input[i]-min_val)
print(profit)
