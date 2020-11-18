n=4

def sumZero(n):
    arr=[0]*n
    
    if n==1:
        return arr
    else:
        for i in range((len(arr)//2)):
            arr[i]=-(i+1)
            arr[-(i+1)]=(i+1)
    return arr

print(sumZero(n))
