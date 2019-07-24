# Reverse Integer
# Easy

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(-x)[::-1])
        inf = pow(2,31)
        if result > inf -1 or result < -inf:
            return 0
        return result