from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_len = len(nums)
        last_el = nums[-1]
        i= 1
        prev = 0
        next = 0

        for i in range(k):
            for j in range(arr_len):
                if(last_el == nums[j]):
                    nums[j] = last_el
                else:
                    nums[j] = nums[j+1]
        print(nums)



        
sol = Solution()

nums = [1,2,3,4,5,6,7]
k = 3

sol.rotate(nums,k)