points=[[1,3], [-2,2]]
K=1

def kClosest(points, K):
    points.sort(key=lambda x:(x[0]**2)+(x[1]**2))
    return points[:K]

print(kClosest(points, K))
