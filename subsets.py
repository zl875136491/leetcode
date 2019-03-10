import itertools


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        for i in range(n+1):
            res += list(itertools.combinations(nums, i))
        return res



nums = [1,2,3]
res=Solution().subsets(nums)
print(res)
