class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)
            if hashmap[nums[i]] >= (len(nums)/2):
                return nums[i]