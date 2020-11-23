words=["abc","deq","mee","aqq","dkd","ccc"]
pattern="abb"

words=["ab","cd","fe","gg"]
pattern="ab"

def findAndReplacePattern(words, pattern):
    ans=[]
    pattern_list=list(pattern)

    type_pat=[]

    for i in range(len(pattern)):
        for j in range(len(pattern_list)):
            if pattern[i]==pattern_list[j]:
                type_pat.append(j)
                break

    for i in range(len(words)):
        set_word=list(words[i])
        type_word=[]
        for k in range(len(words[i])):
            for j in range(len(set_word)):
                if words[i][k]==set_word[j]:
                    type_word.append(j)
                    break
        if type_word == type_pat:
            ans.append(words[i])
        
    return ans

print(findAndReplacePattern(words, pattern))
