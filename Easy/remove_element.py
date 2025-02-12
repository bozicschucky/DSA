from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
               nums.pop(i)
        return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2

sol = Solution()
k = sol.removeElement(nums, val)
print(nums, k)

