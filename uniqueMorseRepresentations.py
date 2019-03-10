class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if(words!=[]):
            res = 0
            k=0
            m=0
            templist = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
            longlist = []
            value = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                     ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
            for i in words:
                for j in i:
                    (j,value[ord(j)-97])
                    k = (k + 1) % int(len(i))
                    templist[m] += value[ord(j)-97]
                m = m + 1
            print(templist[:m])
            for i in templist[:m]:
                for j in range(len(templist[:m])):
                    if(i==templist[j]):
                        res += 1
            return res/(len(templist[:m]))
        else:
            return 0





words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
res = Solution().uniqueMorseRepresentations(words)
print(res)