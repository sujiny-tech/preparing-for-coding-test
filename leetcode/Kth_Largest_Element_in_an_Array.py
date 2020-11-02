import heapq

input_=[3,2,1,5,6,4]
k=2

def findKthLargest(nums, k):
   #solution 1
    heap=[]

    for i in range(len(nums)):
        heapq.heappush(heap, -nums[i])

    answer=0

    for i in range(k):
        answer=heapq.heappop(heap)
    return -answer

   #solution 2
    #heapq.heapify(nums)

    #for _ in range(len(nums)-k):
    #    heapq.heappop(nums)

    #return heapq.heappop(nums)

    #solution 3
    #return heapq.nlargest(k, nums)[-1]

    #solution 4
    #return sorted(nums, reverse=True)[k-1]

print(findKthLargest(input_, k))
