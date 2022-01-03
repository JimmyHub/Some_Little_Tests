#Runtime: 46 ms, faster than 14.50% of Python3 online submissions for Climbing Stairs.
#Memory Usage: 14.3 MB, less than 55.33% of Python3 online submissions for Climbing Stairs.

#題目
# 給予 a,b 2個 2進制字串，將兩者相加後，以2進制返回相加值

def addBinary(a: str, b: str) -> str:
    res = bin(int(a, 2) + int(b, 2))
    return res[2:]



