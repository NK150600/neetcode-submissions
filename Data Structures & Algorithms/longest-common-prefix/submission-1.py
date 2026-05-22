class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word) -> None:
        node = self.root
        for char in word :
            if char not in node.children:
                node.children[char]=TrieNode()
            node = node.children[char]
        
    def lcp(self,word,prefixlen) -> int:
        node = self.root
        for i in range(min(len(word),prefixlen)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word),prefixlen)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]
        
        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i
        
        trie = Trie()
        trie.insert(strs[mini])

        prefixlen = len(strs[mini])
        
        for i in range(len(strs)):
            prefixlen = trie.lcp(strs[i],prefixlen)
        
        return strs[0][:prefixlen]
        
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i==len(s) or s[i] != strs[0][i]:
        #             return s[:i]
        # return strs[0]