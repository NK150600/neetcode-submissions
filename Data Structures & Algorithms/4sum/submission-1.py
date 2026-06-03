class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        left = 0
        right = len(nums)-1
        nums.sort()
        res = []
        # remain = float('inf') 

        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                remain = target - (nums[i]+nums[j])
                left = j+1
                right = len(nums)-1
                while left < right:

                    if nums[left] + nums[right]== remain:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        # right-=1
                        while left < right and nums[left]==nums[left-1]:
                            left+=1
                        # while left < right and nums[right] == nums[right + 1]:
                        #     right -= 1
                    elif nums[left] + nums[right]> remain:
                        right-=1
                    
                    else:
                        left+=1
        
        return res
            

                