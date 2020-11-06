mat=[[1,2,3],[4,5,6],[7,8,9]]

def diagonalSum(mat):
    #solution 2
    ans=0
    for i in range(len(mat)):
        ans+=mat[i][i]+mat[i][-(i+1)]
    if len(mat)%2!=0:
        m=len(mat)//2
        ans-=mat[m][m]
    return ans
    
    #soltuion 1
    #ans=0        
    #for i in range(len(mat)):
    #    for j in range(len(mat[0])):
    #        if i==j or i+j==len(mat)-1:
    #            ans+=mat[i][j]
    #return ans
    
print(diagonalSum(mat))
