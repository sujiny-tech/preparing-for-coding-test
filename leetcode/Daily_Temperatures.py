T = [73, 74, 75, 71, 69, 72, 76, 73]
#T=[89,62,70,58,47,47,46,76,100,70]
#T=[55,38,53,81,61,93,97,32,43,78]
#daily temperatures.
#return a list such that, for each day in the input,
#tells you how many days you would have to wait
#untile a warmer temperature.
#if there is no future day for which this is possible,
#put 0 instead.
#이걸 스택으로?
output=[]#[0]*len(T)
'''
for i in range(len(T)-1):
    for j in range(i+1, len(T)):
        if T[i]<T[j]:
            output[i]=j-i
            break
print(output)
'''
'''
n=len(T)
while len(T)>1:
    val=T.pop(0)
    start=0
    if len(T)>0:
        while start<len(T):
            if val<T[start]:
                output.append(start+1)
                break
            start+=1
        if start==len(T):
            print("here!:", val)
            output.append(0)
    else:
        output.append(0)
output.append(0)
print(output)
'''
'''
output=[]
    while T:
        val=T.pop(0)
        if val+1 in T:
            output.append(T.index(val+1)+1)
        else:
            #val+1차이 없으면 다음+2.
            output.append(0)
    return output
'''

stack=[]
output=[0]*len(T)
for i, cur in enumerate(T):
    while stack and cur>T[stack[-1]]:
        last=stack.pop()
        output[last]=i-last
    stack.append(i)
print(output)