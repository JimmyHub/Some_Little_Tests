#Runtime: 68 ms, faster than 5.12% of Python3 online submissions for Plus One.
#Memory Usage: 14.1 MB, less than 92.02% of Python3 online submissions for Plus One.
# 題目:
# 給一個list 將裡面的數字加總後加1 再分割成每一項 形成新的列表
def plusOne(digits):
    res=0
    total_len = len(digits)
    for i in range(total_len):
        res += 10**(total_len -i-1) * digits[i]
    str_res = str(res+1)
    list_res =[]
    for i in str_res:
        list_res.append(int(i))
    return list_res