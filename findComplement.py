class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res=''
        for i in range(2,len(bin(num))):
            res+=str(1^int(bin(num)[i]))
        return int(res,2)


num=10
res = Solution().findComplement(num)
print(res)