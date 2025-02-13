class TrieNode:
    def __init__(self):
        self.children = {} #Dictionary to store all children
        self.endOfWord = False # Mark the word as end of it

class Trie:

    def __init__(self):
        self.root = TrieNode() #starting point for each node
        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: #If character not present
                cur.children[c] = TrieNode() #Create new node
            cur = cur.children[c] # Move to the next character
        cur.endOfWord = True #Mark the end of the inserted word

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True