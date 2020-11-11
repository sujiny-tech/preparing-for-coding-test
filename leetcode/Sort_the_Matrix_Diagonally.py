mat=[[3,3,1,1],[2,2,1,2], [1,1,1,2]]

def sorting(i, j, mat):
    mid=[]
    a,b=i, j

    while a<len(mat) and b<len(mat[0]):
        mid.append(mat[a][b])
        a+=1
        b+=1
    mid=sorted(mid)

    while mid:
        mat[i][j]=mid.pop(0)
        i+=1
        j+=1

    return mat
    
def diagonalSort(mat):
    for i in range(len(mat)-1):
        mat=sorting(i, 0, mat)
    for j in range(1, len(mat[0])-1):
        mat=sorting(0, j, mat)
        
    return mat

print(diagonalSort(mat))
