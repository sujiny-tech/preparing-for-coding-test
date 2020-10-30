a, b=-2, 3

def getSum(a, b):
    #Another answer
    #MASK=0xFFFFFFFFF
    #INT_MASK=0x7FFFFFFFF
    #while b!=0:
    #    a, b=(a^b)&MASK, ((a&b)<<1)&MASK
    #if a>INT_MASK:
    #    a=~(a^MASK)
    #return a

    arr=[]
    arr.append(a)
    arr.append(b)
    return sum(arr)
    #retrun sum([a,b])

print(getSum(a,b))
