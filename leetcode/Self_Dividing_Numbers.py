left=1
right=22

def selfDividngNumbers(left, right):
    ans=[]
    for num in range(left, right+1):
        list_=list(map(int, str(num)))
        check=True
        for i in list_:
            if i==0 or num%i!=0:
                check=False
                break
        if check:
            ans.append(num)

    return ans

print(selfDividngNumbers(left, right))
