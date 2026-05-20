class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indexed_nums = [[num,i]for i,num in enumerate(nums)]
        # indexed_nums.sort()

        # a = 0
        # b = len(nums)-1

        # while a < b:
        #     curr = indexed_nums[a][0] + indexed_nums[b][0]
        #     if curr == target:
        #         return [min(indexed_nums[a][1],indexed_nums[b][1]),
        #         max(indexed_nums[a][1],indexed_nums[b][1])]
        #     elif curr < target:
        #         a=a+1
        #     else:
        #         b=b-1
        # return []

        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]] = i

        return []