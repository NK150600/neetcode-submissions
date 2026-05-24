class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in range(len(nums)):
            hashset.add(nums[i])
        
        if len(nums) != len(hashset):
            return True

        return False
