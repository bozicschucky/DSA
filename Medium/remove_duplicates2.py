from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ The number of duplicates shouldn't be > 2 and removing the extra elements should be in place"""
        i = 0
        val_dict = {}
        total = 0

        while i < len(nums):
            val = nums[i]
            if val_dict.get(val):
                val_dict[val] = val_dict[val] + 1
            else:
                val_dict[val] = 1
            
            if val_dict[val] > 2:
                nums[i] = 1000000
            i += 1

        nums.sort()
        # print(nums)
        for val in nums:
            if val != 1000000:
                total += 1
      
        return total


sol = Solution()
# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
nums = sol.removeDuplicates(nums)
print(nums)