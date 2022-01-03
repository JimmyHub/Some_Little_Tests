#Runtime: 46 ms, faster than 9.53% of Python3 online submissions for Climbing Stairs.
#Memory Usage: 14.1 MB, less than 72.59% of Python3 online submissions for Climbing Stairs.

#題目
# 給予 階梯的數量n ，每次可以走 1 或 2階，返回所有走法的數量

def climbStairs( n: int) -> int:
    if n < 3:
        return n
    list_res=[0,1,2]
    for i in range(3,n+1,1):
        res = list_res[i-1] +list_res[i-2]
        list_res.append(res)
    return list_res[n]


#Runtime: 53 ms, faster than 5.26% of Python3 online submissions for Climbing Stairs.
#Memory Usage: 14.2 MB, less than 72.59% of Python3 online submissions for Climbing Stairs.
def climbStairs( n: int) -> int:
    if n < 3:
        return n
    res_0 = 1
    res_1 = 2
    res = 0
    for i in range(3,n+1,1):
        res = res_0 + res_1
        res_0 = res_1
        res_1 = res
    return res

## 運算時間太長 無法使用
def climbStairs(self, n: int) -> int:
    if n < 3:
        return n
    res = self.climbStairs(n-1) +self.climbStairs(n-2)
    return res



