class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        def xunhuanchu(num):
            n = len(str(num))
            res1 = []
            for i in range(n):
                res1.append(num%int(i/10**(1)))
            return res1

        for i in range(left,right+1):
            print(xunhuanchu(i))

        return 0




left= 1
right= 22
res = Solution().selfDividingNumbers(left,right)
print(res)