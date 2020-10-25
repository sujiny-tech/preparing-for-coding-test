gas=[1,2,3,4,5]
cost=[3,4,5,1,2]

gas=[3,1,1]
cost=[1,2,2]
fuel, start=0,0

if sum(gas)-sum(cost)<0:
    start=-1

else:
    start, fuel=0,0
    for i in range(len(gas)):
        if gas[i]+fuel<cost[i]:
            print("연료없다, 다시 리셋", fuel)
            start=i+1
            fuel=0
        else:
            fuel+=gas[i]-cost[i]
            print("연로 있다, 다음번으로", fuel)
print(start)