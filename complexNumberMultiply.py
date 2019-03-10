class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def complex_value(c):
            c_first = 0
            c_last = 0

            for i in range(len(c)):
                if (c[i] == '+' and c[i+1]=='-'):
                    c_first = int(c[:i])
                    c_last = -int(c[i+2:-1])

                if (c[i] == '+' and c[i] !='-'):
                    c_first = int(c[:i])
                    c_last = int(c[i+1:-1])

            return c_first,c_last
        a_first,a_last=complex_value(a)
        b_first,b_last=complex_value(b)
        res_first = a_first*b_first-a_last*b_last
        res_last = a_first*b_last+b_first*a_last
        return (str(res_first)+'+'+str(res_last)+'i')


a = "-11+-30i"
b = "55+-69i"
c = "26+42i"
d = "62+-21i"
res = Solution().complexNumberMultiply(a,b)
print(res)