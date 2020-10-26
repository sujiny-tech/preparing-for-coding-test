import collections
input=["eat", "tea", "tan", "ate", "nat", "bat"]
#input=["","",""]

output=[]
anagrams=collections.defaultdict(list)
for word in input:
    anagrams[''.join(sorted(word))].append(word)
print(anagrams.values())
