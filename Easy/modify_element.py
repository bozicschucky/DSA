from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el_dic = {}
        max_el = 0
        max_val = 0
        for i in nums:
            if(el_dic.get(i)):
                el_dic[i] += 1
            else:
                el_dic[i] = 1

        for key in el_dic:
            if(max_val < el_dic[key]):
                max_val = el_dic[key]
                max_el = key
        
        return max_el
            

        