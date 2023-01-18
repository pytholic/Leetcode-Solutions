class Solution(object):
    
    def reverse(self, num):
        return int(str(num)[::-1])
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x >= 0):
            rev = self.reverse(x)
            if (rev == x):
                return True
            else:
                return False
        else:
            return False