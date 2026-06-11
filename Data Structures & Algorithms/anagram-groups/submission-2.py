class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            count = [0]*26
            for j in strs[i]:
                asci = ord(j) - ord('a')
                count[asci]+=1
            hashmap[tuple(count)].append(strs[i])
        
        return (list(hashmap.values()))