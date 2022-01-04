#Runtime: 44 ms, faster than 13.11% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 14.3 MB, less than 24.35% of Python3 online submissions for Pascal's Triangle.
#題目
# 給予1數值 numRows 返回 一個list 內含 相對應層數的list

def generate(numRows: int):
    list_res = []
    if numRows == 0:
        return list_res
    for i in range(numRows):
        list_tmp =[]
        for num in range(i+1):
            if num == 0 or num == (i):
                list_tmp.insert(num,1)
            else:
                num_tmp =list_res[i-1][num-1] +list_res[i-1][num]
                list_tmp.append(num_tmp)
        list_res.append(list_tmp)


generate(5)




