class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            hashmap[nums[i]]= 1+ hashmap[nums[i]]

        for num, count in hashmap.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
            