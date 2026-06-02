class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            temp = 0 - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[right]==temp:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>temp:
                    right-=1
                else:
                    left+=1
        
        return [list(triplet) for triplet in res]
            

        