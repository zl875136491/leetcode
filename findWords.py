class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keys1 =['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        keys2 =['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        keys3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm','Z', 'X', 'C', 'V', 'B', 'N', 'M']
        res = []
        k=0
        def iscontain(words,keys):
            res=[]
            for i in words:
                count = 0
                for j in i:
                    if(j in keys):
                        count+=1
                        if(count==int(len(i))):
                            res.append(i)
            return res
        res+=(iscontain(words, keys1))
        res+=(iscontain(words, keys2))
        res+=(iscontain(words, keys3))
        return res
words =["Hello", "Alaska", "Dad", "Peace"]
res = Solution().findWords(words)
print(res)