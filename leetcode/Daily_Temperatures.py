T = [73, 74, 75, 71, 69, 72, 76, 73]
#T=[89,62,70,58,47,47,46,76,100,70]
#T=[55,38,53,81,61,93,97,32,43,78]
#daily temperatures.
#return a list such that, for each day in the input,
#tells you how many days you would have to wait
#untile a warmer temperature.
#if there is no future day for which this is possible,
#put 0 instead.
output=[]#[0]*len(T)
stack=[]
output=[0]*len(T)
for i, cur in enumerate(T):
    while stack and cur>T[stack[-1]]:
        last=stack.pop()
        output[last]=i-last
    stack.append(i)
print(output)
