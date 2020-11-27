arr= [24,69,100,99,79,78,67,36,26,19]

def peakIndexInMountainArray(arr):

    before=0
    for i in range(len(arr)):
        if i==0:
            before=arr[i]
        else:
            if before>arr[i]:
                return i-1
            else:
                before=arr[i]

    return len(arr)-1

    #same
    #for i in range(len(arr)-1):
    #    return i
    #return len(arr)-1

print(peakIndexInMountainArray(arr))