#Runtime: 55 ms, faster than 5.65% of Python3 online submissions for Remove Element.
#Memory Usage: 14 MB, less than 98.91% of Python3 online submissions for Remove Element.
def removeElement(nums,val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            del nums[i]
    return len(nums)

list01 = [3,2,2,3]
print(removeElement(list01,3))