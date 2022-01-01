
#Runtime: 840 ms, faster than 34.43% of Python3 online submissions for Two Sum.
#Memory Usage: 14.8 MB, less than 91.87% of Python3 online submissions for Two Sum.

#題目: 根據target 找出 在List中 哪兩個值相加會等於target 返回兩個值的index

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums), 1):
        num = target - nums[i]
        if num in nums:
            if nums.index(num) != i:
                return [i, nums.index(num)]

#Runtime: 4056 ms, faster than 22.92% of Python3 online submissions for Two Sum.
#Memory Usage: 14.8 MB, less than 80.25% of Python3 online submissions for Two Sum.
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0,len(nums)-1,1):
        for u in range(i+1,len(nums),1):
            if nums[i] + nums[u] == target :
                return [i,u]
