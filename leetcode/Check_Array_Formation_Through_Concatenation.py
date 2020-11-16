arr=[12,21,11,22]
pieces=[[12,21],[1,2]]

def canFormArray(arr, pieces):
    answer = True

    while pieces:
        p = pieces.pop(0)
        #len(piece[i])==1
        if len(p) == 1 and p[0] in arr:
            continue
        else:
            #len(piece[i])>=2
            l=len(p)
            if p[0] not in arr:
                return False

            ind=arr.index(p[0])

            if arr[ind:ind+l]==p:
                continue
            else:
                return False




    return answer

print(canFormArray(arr, pieces))