
#Runtime: 24 ms, faster than 94.85% of Python3 online submissions for Number Complement.
#Memory Usage: 14.2 MB, less than 41.72% of Python3 online submissions for Number Complement.
def findComplement(self, num: int) -> int:
    temp = bin(num)[3:]
    res = 0
    for i in range(0, len(temp)):
        if temp[i] == '0':
            res += 2 ** (len(temp) - i - 1)
    return res

#Runtime: 32 ms, faster than 55.58% of Python3 online submissions for Two Sum.
#Memory Usage: 14.1 MB, less than 88.47% of Python3 online submissions for Two Sum.
def findComplement(self, num: int) -> int:
    temp = '{0:b}'.format(num)
    res = 0
    for i in range(len(temp)):
        if temp[i] == '0':
            res += 2 ** (len(temp) - i - 1)
    return res
