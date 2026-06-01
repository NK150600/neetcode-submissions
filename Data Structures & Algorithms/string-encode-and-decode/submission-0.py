class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        
        return s

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:1+j+length])

            i = 1+j+length

        return res
            

