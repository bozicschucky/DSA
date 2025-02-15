from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        next = 1
        count = 1

        while next < len(nums): 
            if nums[prev] != nums[next]:
                count += 1
                prev += 1
                nums[prev] = nums[next]
            
            next = next + 1
        nums[:] = nums[:count] 
        print(nums)
        return count

            
        


sol = Solution()
nums = [1,1,2]

k = sol.removeDuplicates(nums)
print(k)

# out put
[1,2,2]
