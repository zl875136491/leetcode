class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        act = [2, 3, 4, 5, 6]
        for i in act:
            if(n==1 or n==2):
                return True
            else:
                if(n%i==1):
                    return True
                else:
                    return False





n = 6
res = Solution().canWinNim(n)
print(res)