#import collections
s="abcabcbb"
def lengthOfLongestSubstring(s:str)-> int:
    max_len=0
    used= {}

    if len(set(list(s)))<=1:
        return len(set(list(s)))

    start=0
    for index, char in enumerate(s):
        if char in used and start<=used[char]:
            start=used[char]+1
        else:
            max_len=max(max_len, index-start+1)
        used[char]=index
    #print(max_len)
    return max_len
print(lengthOfLongestSubstring(s))