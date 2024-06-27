class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.nodes = {}

class WordDictionary:

    def __init__(self):
        # self.head = TrieNode()
        self.dict = {}
        self.cache = {}
        

    def addWord(self, word: str) -> None:
        index = len(word)
        if index not in self.dict:
            self.dict[index] = []
        self.dict[index].append(word)
        # curr = self.head
        # Create a TrieNode for "." and set for the next word
        # n = len(word)
        # prevTrieNode = None
        # for i in range(0, n):
        #     c = word[i]
        #     if c not in curr.nodes:
        #         curr.nodes[c] = TrieNode()
        #         if prevTrieNode is not None:
        #             # curr.nodes[c].nodes["."] = 
        #             prevTrieNode.nodes["."] = curr.nodes[c]
        #     prevTrieNode = curr
        #     curr = curr.nodes[c]
        # for i in range(0, n-1):
        #     c = word[i]
        #     nextC = word[c + 1]
        #     if c not in curr.nodes:
        #         curr.nodes[c] = TrieNode(nextC)
        #     curr = curr.nodes[c]
        
        # curr.nodes[word[n-1]] = TrieNode(None)
        # curr.wordEnd = True
        
    def search(self, word: str) -> bool:
        
        def isSame(word1, word2):
            n = len(word1)
            for i in range(n):
                c1, c2 = word1[i], word2[i]
                if (c1 != "." and c2 != ".") and c1 != c2:
                    return False
            return True
        
        if word in self.cache:
            return True
        index = len(word)
        if index in self.dict:
            for storedWord in self.dict[index]:
                if isSame(word, storedWord):
                    self.cache[word] = True
                    return True
                    
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
word = "bad"
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("bid")
param_2 = obj.search("b.d")
print(param_2)
