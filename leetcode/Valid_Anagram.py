import collections

t="anagram"
s="nagaram"

def isAnagram(str1, str2):
    cnt_s=collections.Counter(str1)
    cnt_t=collections.Counter(str2)
    
    if cnt_s==cnt_t:
        return True
    else:
        return False
        
    #solution 2
    #if sorted(str1)==sorted(str2):
    #    return True
    #else:
    #    return False
