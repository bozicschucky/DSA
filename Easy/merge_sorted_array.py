from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [i for i in nums1 if i != 0]
        m = n + m 
        for i in range(n):
            for j in range(m):
                if(nums1[j] == 0 ):
                    nums1[j] = nums2[i]
                    break
        nums1.sort()
        # return nums1




nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


sol = Solution()
nums = sol.merge(nums1, m, nums2, n)
# print(nums)
print(nums1)
expected_output  = [1,2,2,3,5,6]