intervals=[[1,3],[2,6],[8,10],[15,18]]
#[[1,4],[4,5]]

def merge(intervals):
    intervals=sorted(intervals, key=lambda x:x[0])
    merged=[]
    for inter in intervals:
        if merged and inter[0]<=merged[-1][1]:
            merged[-1][1]=max(merged[-1][1], inter[1])
        else:
            merged+=inter,
    return merged

print(merge(intervals))