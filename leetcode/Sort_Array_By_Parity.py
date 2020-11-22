
A=[0,1,2,4]

def sortArrayByParity(A):
    # solution 1.
    even = []
    odd = []

    for num in A:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd

    '''
    #solution 2.
    l=len(A)
    start, end=0, l-1
    while start<end:
        if A[start]%2==0:
            start+=1
        else:
            num=A.pop(start)
            if end==len(A)-1:
                end-=1
            A.append(num)
        if A[end]%2!=0:
            end-=1
        else:
            num=A.pop(end)
            if start==0:
                start+=1
            A.insert(0, num)
    return A
    '''


print(sortArrayByParity(A))
