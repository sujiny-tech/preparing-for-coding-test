from itertools import permutations

def solution(babbling):
    answer=0
    check = ["aya", "ye", "woo", "ma"]
    permutation_total = []
    
    for i in range(1, len(check)+1):
        for j in permutations(check, i):
            permutation_total.append("".join(j))
            
            
    for i in babbling:
        if i in permutation_total:
            answer+=1
            
    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
