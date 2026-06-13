class TrieNode:
    def __init__(self) :
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]= TrieNode()
            node = node.children[char]
    
    def lcp(self,word,prefix):
        node = self.root
        for i in range(min(len(word),prefix)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word),prefix)




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==1:
            return strs[0]
        
        mini = 0

        for i in range(1,len(strs)):
            if len(strs[mini])> len(strs[i]):
                mini = i
        
        trie = Trie()

        trie.insert(strs[mini])

        prefixlength = len(strs[mini])

        for i in range(len(strs)):
            prefixlength = trie.lcp(strs[i],prefixlength)
        
        return strs[0][:prefixlength]

