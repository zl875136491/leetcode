class Solution(object):
    def reverseString(self, s):
        a = s[::-1]
        return a

s = "hello"
res = Solution().reverseString(s)
print(res)