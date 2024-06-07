class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False    
            node = node.children[char]
        
        if node.isEnd:
            return True
        
        return False
        
        
        
        
    
    def startWith(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True



tri = Trie()

tri.insert("apple")
tri.insert("appreciate")
tri.insert("bromite")


print(tri.search("apple"))
print(tri.startWith("appr"))
print(tri.startWith("c"))
print(tri.startWith("b"))


