class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.nodes = {}

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()
        # self.dict = {}
        # self.cache = {}
        

    def addWord(self, word: str) -> None:
        curr = self.head
        # Create a TrieNode for "." and set for the next word
        n = len(word)
        for i in range(0, n):
            c = word[i]
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
            curr = curr.nodes[c]
        curr.wordEnd = True
        
    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index):
            if index == len(word):
                return node.wordEnd
            c = word[index]
            if c in node.nodes:
                return dfs(node.nodes[c], index + 1)
            elif c == ".":
                for key, val in node.nodes.items():
                    if dfs(val, index + 1):
                        return True
                    
            return False
        
        return dfs(self.head, 0)
        


# Your WordDictionary object will be instantiated and called as such:
word = "bad"
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("bid")
param_2 = obj.search("b.d")
print(param_2)
