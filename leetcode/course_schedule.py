import collections
num_courses=3
prerequisites=[[1,0], [0,2], [2,1]]

def canFinish(numCourses, prerequisites):
    results=[]
    graph=collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)
    print(graph)

    traced=set()
    visited=set()

    def dfs(i):
        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True

print(canFinish(num_courses, prerequisites))
