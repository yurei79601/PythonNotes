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

