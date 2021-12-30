#Runtime: 36 ms, faster than 10.53% of Python online submissions for Longest Common Prefix.
#Memory Usage: 13.7 MB, less than 66.34% of Python online submissions for Longest Common Prefix.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word = ''
        word_res = ''
        for w in range(len(strs[0])):
            word += strs[0][w]
            count = 0
            for i in strs:
                if word in i:
                    if i.startswith(word):
                        count += 1
            if count == len(strs):
                word_res += strs[0][w]
        if word_res != '':
            return word_res
        return ""
