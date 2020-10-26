import collections
import heapq

#n : citiies
#m : flights -->there are n cities connected by m flights.
#each flight starts from city u and arries at v with a price w.
#u->v (price w)
#to find the cheapest price from src(starting city) to dst(destination) with up to k stops,
#if there is no such route, output -1

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1 #0

def findCeahpestPrice(n, flights, src, dst, K):
    graph=collections.defaultdict(list)
    for u, v, cost in flights:
        graph[u].append((v, cost, 1))

    Q=[(0, src, 0)] #cost, start, k
    dist=collections.defaultdict(int)

    while Q:
        cost, node, mid = heapq.heappop(Q)
        if node not in dist:
            dist[node]=cost
            for v, c, m in graph[node]:
                alt=cost+c
                if v==dst:
                    mid=1
                else:
                    mid+=m
                heapq.heappush(Q, (alt, v, mid))

    return dist[dst]

print(findCeahpestPrice(n, edges, src, dst, k))
