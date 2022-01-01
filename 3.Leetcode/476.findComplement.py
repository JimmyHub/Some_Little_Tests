
#Runtime: 24 ms, faster than 94.85% of Python3 online submissions for Number Complement.
#Memory Usage: 14.2 MB, less than 41.72% of Python3 online submissions for Number Complement.

#題目: 將num轉換成 2進制 然後返回跟其2進制互補的數值
# 例如 給定值為5 2進制為 101 ，互補為 010 值為2 返回2
# 若 給定值為 1
def findComplement( num: int) -> int:
    temp = bin(num)[3:]
    res = 0
    for i in range(0, len(temp)):
        if temp[i] == '0':
            res += 2 ** (len(temp) - i - 1)
    return res

#Runtime: 32 ms, faster than 55.58% of Python3 online submissions for Two Sum.
#Memory Usage: 14.1 MB, less than 88.47% of Python3 online submissions for Two Sum.
def findComplement(num: int) -> int:
    temp = '{0:b}'.format(num)
    res = 0
    for i in range(len(temp)):
        if temp[i] == '0':
            res += 2 ** (len(temp) - i - 1)
    return res
