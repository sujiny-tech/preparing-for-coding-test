from itertools import product
digits="23"
letters={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz",}

def letterCombinations(digits):
    def dfs(index, path):
        if len(path)==len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in letters[digits[i]]:
                dfs(i+1, path+j)

    if not digits:
        return []
    result=[]
    dfs(0, "")
    return result

print(letterCombinations(digits))
