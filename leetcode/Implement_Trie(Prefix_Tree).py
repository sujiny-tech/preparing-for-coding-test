import collections

class Node:
    def __init__(self):
        self.word=False
        self.child=collections.defaultdict(Node)
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=Node()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root=self.head
        for w in word:
            root=root.child[w]
        root.word=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root=self.head
        for w in word:
            if w not in root.child:
                return False
            root=root.child[w]
        return root.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root=self.head
        for w in prefix:
            if w not in root.child:
                return False
            root=root.child[w]
        return True
        

trie=Trie()

trie.insert("apple")
param1=trie.search("apple")
param2=trie.search("app")
param3=trie.startsWith("app")
trie.insert("app")
param4=trie.search("app")
