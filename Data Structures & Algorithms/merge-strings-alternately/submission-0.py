class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        left_str = 0
        right_str = 0
        newStr = ""

        while left_str<len(word1) and right_str<len(word2) : 
            newStr += word1[left_str]
            newStr += word2[right_str]
            left_str+=1
            right_str+=1
        
        if left_str!=len(word1):
            newStr += word1[left_str:len(word1)]
                    
        if right_str!=len(word2):
            newStr += word2[right_str:len(word2)]
        

        return newStr


        