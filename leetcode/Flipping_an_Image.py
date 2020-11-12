A=[[1,1,0],[1,0,1],[0,0,0]]

def flipAndInvertImage(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]=(A[i][j]+1)%2

    return [x[::-1] for x in A]

print(flipAndInvertImage(A))