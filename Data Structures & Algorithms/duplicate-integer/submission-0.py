class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = 0
        b = 1
        nums.sort()
        while a <= len(nums)-2:
            if nums[a]==nums[a+1]:
                return True
            else:
                a=a+1
        return False


