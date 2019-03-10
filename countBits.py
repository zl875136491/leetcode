class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r=[]
        for i in range(num+1):
            s = str(bin(i))
            r.append(s.count('1'))
        return r


res = Solution().countBits(4)
print(res)