class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.nodes = {}

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        # Create a TrieNode for "." and set for the next word
        n = len(word)
        prevTrieNode = None
        for i in range(0, n):
            c = word[i]
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
                if prevTrieNode is not None:
                    # curr.nodes[c].nodes["."] = 
                    prevTrieNode.nodes["."] = curr.nodes[c]
            prevTrieNode = curr
            curr = curr.nodes[c]
        # for i in range(0, n-1):
        #     c = word[i]
        #     nextC = word[c + 1]
        #     if c not in curr.nodes:
        #         curr.nodes[c] = TrieNode(nextC)
        #     curr = curr.nodes[c]
        
        # curr.nodes[word[n-1]] = TrieNode(None)
        curr.wordEnd = True
        
    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
                
            if c not in curr.nodes:
                return False
            
            curr = curr.nodes[c]
        return curr.wordEnd
        


# Your WordDictionary object will be instantiated and called as such:
word = "bad"
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("bid")
param_2 = obj.search("b.d")
print(param_2)
