#Runtime: 27 ms, faster than 18.65% of Python online submissions for Valid Parentheses.
#Memory Usage: 13.7 MB, less than 35.10% of Python online submissions for Valid Parentheses.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    res_2 = []
    dict_pair = {'(': ')', '{': '}', '[': ']'}
    ans_b = False
    for i in range(len(s)):
        try:
            ans = dict_pair[s[i]]
            res_2.append(ans)
            print(res_2)
        except:
            if res_2 != []:
                print(s[i])
                print(res_2)
                check_res = res_2.pop()
                if check_res == s[i]:
                    ans_b = True
                else:
                    ans_b = False
                    break
            else:
                ans_b =False
                break
        if res_2:
            return False
    return ans_b

print(isValid(str02))