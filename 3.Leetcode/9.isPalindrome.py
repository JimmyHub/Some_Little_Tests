#Runtime: 60 ms, faster than 46.01% of Python online submissions for Palindrome Number.
#Memory Usage: 13.5 MB, less than 38.67% of Python online submissions for Palindrome Number.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x =str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[-i-1]:
                return False
        return True

#Runtime: 68 ms, faster than 30.57% of Python3 online submissions for Number Complement.
#Memory Usage: 13.5 MB, less than 38.67% of Python3 online submissions for Number Complement.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list_x = []
        list_v = []
        str_x = str(x)
        for i in range(len(str_x)):
            list_x.append(str_x[i])
            list_v.append(str_x[-i - 1])
        if list_x == list_v:
            return True
        return False

#Runtime: 100 ms, faster than 8.95% of Python3 online submissions for Two Sum.
#Memory Usage: 13.4 MB, less than 67.43% of Python3 online submissions for Two Sum.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list_x=[]
        list_v=[]
        for i in range(len(str(x))):
            list_x.append(str(x)[i])
            list_v.append(str(x)[-i-1])
        if list_x == list_v:
            return True
        return False
