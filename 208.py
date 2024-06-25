from typing import List


class TrieNode:
    
    def __init__(self):
        self.wordEnd = False
        self.childNode = {}
      
def getCharDiff(a, b):
    return ord(a) - ord(b)

class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.head
        for c in word:
            # charIndex = getCharDiff(c, 'a')
            # if currNode.childNode[charIndex] is None:
            if c not in currNode.childNode:
                currNode.childNode[c] = TrieNode()
            currNode = currNode.childNode[c]

        currNode.wordEnd = True

    def search(self, word: str) -> bool:
        currNode = self.head
        for c in word:
            # charIndex = getCharDiff(c, 'a')
            # if currNode.childNode[charIndex] is None:
            if c not in currNode.childNode:
                return False
            currNode = currNode.childNode[c]

        return currNode.wordEnd

    def startsWith(self, prefix: str) -> bool:
        currNode = self.head
        for c in prefix:
            # charIndex = getCharDiff(c, 'a')
            # if currNode.childNode[charIndex] is None:
            if c not in currNode.childNode:
                return False
            currNode = currNode.childNode[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)