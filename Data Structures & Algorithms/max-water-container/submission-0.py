class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights)-1
        max_amount = 0

        while left < right:
            capacity = (right-left)* min(heights[left],heights[right])
            max_amount = max(max_amount,capacity)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        
        return max_amount
            

        