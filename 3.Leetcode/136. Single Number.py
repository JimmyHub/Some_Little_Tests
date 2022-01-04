#Runtime: 136 ms, faster than 52.71% of Python3 online submissions for Single Number.
#Memory Usage: 16.8 MB, less than 19.05% of Python3 online submissions for Single Number.

#題目
# 給予list 內含不定數量跟順序的數字， 最終返回沒有重複的數字
def singleNumber(nums) -> int:
    dict_res = {}
    for i in nums:
        num = dict_res.get(i, 0)
        if num:
            dict_res[i] = num + 1
        else:
            dict_res[i] =1
    for i in dict_res:
        if dict_res[i] == 1:
            return i
singleNumber([2,2,1])




