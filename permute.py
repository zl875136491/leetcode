import itertools

import math


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n=int(len(nums))
        for i in itertools.permutations(nums,n):
            res.append(i)
        return res











nums =[1,2,3]
res =Solution().permute(nums)
print(res)
