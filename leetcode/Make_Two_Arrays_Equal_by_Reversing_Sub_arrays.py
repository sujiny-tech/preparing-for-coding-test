import heapq

target=[3, 7, 9]#[718, 745, 231, 697]#[1,1,1,1,1]#[1,2,3,4]
arr=[3, 7, 11]#[697, 718, 231, 745]#[1,1,1,1]#[2,4,1,3]

def canBeEqual(target, arr):
    #return sorted(target)==sorted(arr)

    #solution 2
    heapq.heapify(target)
    heapq.heapify(arr)

    while target:
        t=heapq.heappop(target)
        a=heapq.heappop(arr)
        if t!=a:
            return False
    return True

print(canBeEqual(target, arr))