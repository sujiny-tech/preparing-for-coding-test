grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

def countNegatives(grid):
    all_ = []
    for i in range(len(grid)):
        all_ += grid[i]

    all_ = [x < 0 for x in sorted(all_)]
    return all_.count(True)

    '''
    #solution 2.
    ans=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]<0:
                ans+=1
    return ans
    '''

    '''
    #solution 1.
    ans=0
    while grid:
        g=grid.pop(0)
        g=sorted(g)
        for i in range(len(g)):
            if g[i]>=0:
                break
            else:
                ans+=1
    return ans
    '''


print(countNegatives(grid))
