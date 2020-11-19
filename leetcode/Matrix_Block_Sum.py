mat=[[1,2,3], [4,5,6], [7,8,9]]
k=1
mat=[[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
k=3
def matrixBlockSum(mat, k):
    ans=[]
    for i in range(len(mat)):
        row=[]
        for j in range(len(mat[0])):
            r=max(i-k, 0)
            c=max(j-k, 0)
            mid=0
            r_max=min(len(mat), i+k+1)
            c_max=min(len(mat[0]), j+k+1)
            for r1 in range(r, r_max):
                for c1 in range(c, c_max):
                    mid+=mat[r1][c1]
            row.append(mid)
        ans.append(row)

    return ans

print(matrixBlockSum(mat, k))
