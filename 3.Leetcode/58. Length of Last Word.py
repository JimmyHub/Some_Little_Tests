# Runtime: 36 ms, faster than 20.53% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.3 MB, less than 64.70% of Python3 online submissions for Length of Last Word.

# 題目:
# 找到字串s中最後一個單字 並返回單字長度
def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(' ')[-1])