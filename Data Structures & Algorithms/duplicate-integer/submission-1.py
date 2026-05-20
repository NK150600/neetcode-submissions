class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a = 0
        # b = 1
        # nums.sort()
        # while a <= len(nums)-2:
        #     if nums[a]==nums[a+1]:
        #         return True
        #     else:
        #         a=a+1
        # return False
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


