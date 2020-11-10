n, m=28, 38
indices=[[17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],[23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]]
#[[0,1],[1,1]]


def oddCells(n, m, indices):
    arr=[[0]*m for i in range(n)]
    for indice in indices:
        for i in range(m):
            arr[indice[0]][i]+=1
        for j in range(n):
            arr[j][indice[1]]+=1

    c=[]
    for i in range(len(arr)):
        c+=arr[i]
    c=[x %2!=0 for x in c]

    return c.count(True)

print(oddCells(n,m, indices))