n=0b00000000000000000000000000001011

def hammingWeight(n: int) -> int:
    return bin(n).count('1')

    #Another answer
    #cnt=0
    #while n:
    #    n=n&(n-1)
    #    cnt+=1
    #return cnt

print(hammingWeight(n))
