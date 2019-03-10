class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        r = 0
        for move in moves:
            if (move == 'D' or move == 'L'):
                r -= 1
            if (move == 'U' or move == 'R'):
                r += 1
        if(r==0):
            return True
        else:
            return False


res=Solution().judgeCircle(input())
print(res)