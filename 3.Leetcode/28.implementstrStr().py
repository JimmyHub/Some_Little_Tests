#Runtime: 45 ms, faster than 60.71% of Python3 online submissions for Implement strStr().
#Memory Usage: 14.4 MB, less than 84.83% of Python3 online submissions for Implement strStr().

# 題目: 判斷needle 是否有在 haystack中
# 如果有 則返回needle 這個詞第一個在haystack 中出現的index
# 如果沒有 則返回-1
# 如果needle="" 則返回0
def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    elif needle in haystack:
        index_str = haystack.index(needle)
        return index_str
    else:
        return -1