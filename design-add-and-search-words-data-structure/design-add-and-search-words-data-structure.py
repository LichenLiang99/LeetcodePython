class TrieNode:
    
    def __init__(self):
        self.child = {}
        self.endWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.endWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for children in curr.child.values():
                        if dfs(i + 1, children):
                            return True
                    return False
                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
                    
            return curr.endWord
            
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)