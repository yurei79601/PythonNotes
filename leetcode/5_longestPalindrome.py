def is_palindromic(a_string):
    return a_string == a_string[::-1]


class Solution:
    def longestPalindrome(self, a_string: str) -> str:
        if len(a_string) in [0, 1]:
            return a_string

        if is_palindromic(a_string):
            return a_string

        string_length = len(a_string)

        for i in range(1, string_length):

            j = string_length - i
            for k in range(i+1):
                sub_string = a_string[k: k+j]
                if is_palindromic(sub_string):
                    return sub_string


## 以下通過的版本


def create_dp_table(table_size):
    """
    根據字元長度建立 dynamic table
    """
    dp_table = [[0] * table_size for _ in range(table_size)]
    for i in range(table_size):
        dp_table[i][i] = True
    return dp_table


def is_palindromic(a_string):
    """
    直接檢查這個字串是不是迴字
    """
    return a_string == a_string[::-1]


class Solution:
    """
    通過的解法
    參考 https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP
    """
    def longestPalindrome(self, a_string: str) -> str:
        if len(a_string) in [0, 1]:
            return a_string

        if is_palindromic(a_string):
            return a_string

        string_length = len(a_string)
        dp_table = create_dp_table(string_length)

        longest_one = a_string[0]
        for k in range(1, string_length):
            # 從 sub_string 字元長度 +1 開始滾到原始字元的長度
            for i in range(string_length - k):
                if k == 1:
                    # 2 個字元的 case 比較特別
                    if a_string[i] == a_string[i+k]:
                        dp_table[i][i+k] = True
                        longest_one = a_string[i:i+k+1]
                else:
                    j = i + k
                    # 開始去滾 dynamic table
                    # 檢查 a_string[i:j] 的狀況
                    if a_string[i] == a_string[j]:
                        # 第一個條件：第一格字元 = 最後一個字元
                        if dp_table[i+1][j-1]:
                            # 第二個條件：檢查前一個狀態是不是迴字
                            dp_table[i][j] = True
                            if len(a_string[i:j+1]) > len(longest_one):
                                longest_one = a_string[i:j+1]
        return longest_one, dp_table