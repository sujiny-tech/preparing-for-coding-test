import itertools
candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 8
#candidates=[7,3,2]
#target=18

def combinationSum(candidates, target):
    results = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            results.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return results


print(combinationSum(candidates, target))
