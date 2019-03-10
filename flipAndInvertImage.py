class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        k=2
        B=[]
        for i in A:
            i.reverse()
            for j in interi:
                k = (k + 1) % len(i)
                if(i[k]==1):
                    i[k]=0
                elif(i[k]==0):
                    i[k]=1


                print(k)
        return A



exmple = [[1,1,0],[1,0,1],[0,0,0]]
res = Solution().flipAndInvertImage(exmple)
print(res)