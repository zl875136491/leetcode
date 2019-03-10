class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        n=max(len(bin(x)),len(bin(y)))-1
        print(bin(x), bin(y),n)
        for i in range(1,n):
            if(bin(x)[-i]!=bin(y)[-i]):
                res+=1

        return res-1



x = 1
y = 4
res = Solution().hammingDistance(x, y)
print(res)