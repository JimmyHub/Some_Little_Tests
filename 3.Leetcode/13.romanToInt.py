#Runtime: 24 ms, faster than 98.47% of Python online submissions for Roman to Integer.
#Memory Usage: 13.4 MB, less than 61.95% of Python online submissions for Roman to Integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        last = ''
        for i in range(len(s)):
            num = s[-i-1]
            if num == 'I':
               if last =="V" or last =="X":
                   res -=1
               else:
                   res +=1
                   last = num
            elif num == 'V':
                res +=5
                last = num
            elif num == 'X':
                if last == "C" or last == "L":
                    res -= 10
                else:
                    res += 10
                    last = num
            elif num == 'L':
                res +=50
                last = num
            elif num == 'C':
                if last == "M" or last == "D":
                    res -= 100
                else:
                    res += 100
                    last = num
            elif num == 'D':
                res +=500
                last = num
            elif num == 'M':
                res += 1000
                last = num
        return res 