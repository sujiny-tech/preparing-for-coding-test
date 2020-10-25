import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
paragraph=re.sub('[^\w]', ' ', paragraph)
for ban in banned:
    paragraph=re.sub('{}'.format(ban), '', paragraph)
paragraph=paragraph.lower()

word=paragraph.split()
cnt=[]
for w in word:
    cnt.append(word.count(w))
print(word)
print(cnt)
m=max(cnt)

print(word[cnt.index(m)])

'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.sub('[^\w]', ' ', paragraph)
        paragraph=paragraph.lower()
        for ban in banned:
            paragraph=re.sub('{}'.format(ban.lower()), '', paragraph)
        
        word=paragraph.split()
        cnt=[]
        for w in word:
            cnt.append(word.count(w))
        m=max(cnt)
        return word[cnt.index(m)]
        '''