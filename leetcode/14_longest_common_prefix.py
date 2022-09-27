"""
找出一個 list of string 裡面，大家共同的開頭字串
"""
from typing import List


def find_common_character(string_list, i):
    try:
        this_word = string_list[0][i]
        for a_string in string_list[1:]:
            if a_string[i] not in this_word:
                this_word += a_string[i]
                return this_word
    except IndexError:
        return "AB"
    return this_word


def main(string_list):
    if len(string_list) == 1:
        return string_list[0]
    common_prefix = ""
    i = 0
    while True:
        common_character = find_common_character(string_list, i)
        if len(common_character) == 1:
            common_prefix += common_character
        else:
            break
        i += 1
    return common_prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return main(strs)
