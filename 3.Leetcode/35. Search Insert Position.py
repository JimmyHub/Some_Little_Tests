#Runtime: 44 ms, faster than 91.57% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15 MB, less than 81.87% of Python3 online submissions for Search Insert Position.

#題目:
# 如果target 有在List中 則直接返回 target的index
# 如果沒有 則返回 target應該插入在哪個index的位置
def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    idx = 0
    for i in nums:
        if target > i:
            idx += 1
    return idx