s="Let's take LeetCode contest"

def reverseWords(s):
    split_s=s.split(' ')
    split_s=[s[::-1] for s in split_s]
    
    return ' '.join(split_s)
    
print(reverseWords(s))
