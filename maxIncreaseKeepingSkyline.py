class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = 0
        index = index2 = 0
        for i in grid:
            for j in i:
                r += int(min(max(grid[index]), max([x[index2] for x in grid]))) - j
                index2 = (index2 + 1) % len(i)
            index += 1
        return r



grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]
res = Solution().maxIncreaseKeepingSkyline(grid)
print(res)