#Runtime: 129 ms, faster than 27.13% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.7 MB, less than 47.04% of Python3 online submissions for Remove Duplicates from Sorted Array.

def removeDuplicates(nums: List[int]) -> int:
    dict_res = {}
    for i in nums:
        score = dict_res.get(i, 0)
        if score == 0:
            dict_res[i] = 1
        else:
            dict_res[i] += 1
    print(dict_res)
    k = 0
    for key in dict_res:
        nums[k] = key
        k += 1
    for re in range(len(nums)):
        if re > k - 1:
            nums[re] = '_'
    return nums
#Runtime: 92 ms, faster than 41.52% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.7 MB, less than 47.04% of Python3 online submissions for Remove Duplicates from Sorted Array.

def removeDuplicates(nums: List[int]) -> int:
    dict_res = {}
    for i in nums:
        score = dict_res.get(i, 0)
        if score == 0:
            dict_res[i] = 1
        else:
            dict_res[i] += 1
    k = 0
    for key in dict_res:
        nums[k] = key
        k += 1
    return k


