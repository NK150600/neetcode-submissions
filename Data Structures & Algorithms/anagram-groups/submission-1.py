class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            count =[0]*26
            for char in  word:
                value = ord(char)-ord('a')
                count[value]+=1
            hashmap[tuple(count)].append(word)
        
        return list(hashmap.values())
