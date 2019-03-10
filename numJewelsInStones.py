



class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        r=0
        for j in J:
            r+= S.count(j)
        return r
J = "aA"
S = "aAAbbbb"
res = Solution().numJewelsInStones(J,S)
print(res)

