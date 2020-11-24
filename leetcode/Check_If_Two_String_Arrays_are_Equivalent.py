word1=["ab", "c"]
word2=["a", "bc"]

def arrayStringsAreEqual(word1, word2):
    w1, w2="", ""
    
    for w in word1:
        w1+=w

    for w in word2:
        w2+=w

    return w1==w2

print(arrayStringsAreEqual(word1, word2)
