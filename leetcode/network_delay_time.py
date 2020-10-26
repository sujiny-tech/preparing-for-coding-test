#dijkstra algorithm
import collections
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

def networkDelayTime(times, N, K):
    graph=collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    Q=[(0,K)]
    dist=collections.defaultdict(int)
    while Q:
        time, node=heapq.heappop(Q)
        if node not in dist:
            dist[node]=time
            for v, w in graph[node]:
                alt=time+w 
                heapq.heappush(Q, (alt, v))
    if len(dist)==N:
        return max(dist.values())
    else:
        return -1

print(networkDelayTime(times, N,K))
