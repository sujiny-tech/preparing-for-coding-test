arr=[3,0,1,1,9,7]
a,b,c=7,2,3

def countGoodTriplets(arr, a, b, c):
    cnt=0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                    cnt+=1
    return cnt

print(countGoodTriplets(arr, a, b, c))
