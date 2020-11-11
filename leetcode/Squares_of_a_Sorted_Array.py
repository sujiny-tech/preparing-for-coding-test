A=[-4, -1, 0, 3, 10]
#A=[-7, -3, 2, 3, 11]

def sortedSquares(A):
    return sorted([x**2 for x in A])

    #A=sorted(A, key=lambda x:x**2)
    #return [x**2 for x in A]

print(sortedSquares(A))
