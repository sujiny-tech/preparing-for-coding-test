num=8

def numberOfSteps(num):
    cnt=0
    while num:
        if num%2==0:
            num/=2
            cnt+=1
        else:
            num-=1
            cnt+=1
    return cnt

print(numberOfSteps(num))
