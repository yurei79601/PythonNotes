"""
羅列出字串中所有英文字母大小寫的排列 cases
"""
from typing import List
import re
from copy import deepcopy
import string


alphabeta_dict = {
    string.ascii_lowercase[i]: {
        0: string.ascii_lowercase[i],
        1: string.ascii_uppercase[i]
    }
    for i in range(len(string.ascii_lowercase))
}


def append_one_case(a_list):
    """
    讓 a_list 再根據下一個狀況有 0, 1 增長 case
    """
    b_list = deepcopy(a_list)
    for i, case_list in enumerate([a_list, b_list]):
        for sub_list in case_list:
            sub_list.append(i)
    a_list.extend(b_list)
    return a_list


def get_power_set_list(order):
    """
    取得所有深度為 order 的發展狀況
    本案例為二元分類 (大寫小寫)，所以以 [0, 1] 表示

    Example:
        order = 2
        loop_list = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    """
    loop_list = [[]]
    for _ in range(order):
        loop_list = append_one_case(loop_list)
    return loop_list


def get_one_case_map_result(english_string, one_case_list):
    """
    使用 one_case_list 來將 english_string 裡面字串的大小寫改變

    Example:
        english_string = 'abc'
        one_case_list = [0, 1, 0]
        output = 'aBc'
    """
    return "".join(
        [alphabeta_dict[english_string[i]][one_case_list[i]] for i, _ in enumerate(english_string)]
    )


def get_all_alphabeta(a_string):
    """
    取得字串中所有包含英文字的
    1. 位置起點與終點
    2. 匹配的英文字
    因為可能有多個，所以皆以 list 表示
    """
    index_list, match_list = [], []
    start_index = 0
    while re.search("\D+", a_string[start_index:]):
        re_result = re.search("\D+", a_string[start_index:])
        key_tuple = (start_index + re_result.span()[0], start_index + re_result.span()[1])
        start_index += re_result.span()[-1]
        index_list.append(key_tuple)
        match_list.append(re_result.group())
    return index_list, match_list


def get_all_case_for_string(english_string):
    """
    取得一個字串 (純英文字) 中所有大小寫的例子
    """
    power_set_list = get_power_set_list(len(english_string))
    all_case = []
    for one_case_list in power_set_list:
        all_case.append(get_one_case_map_result(english_string, one_case_list))
    return all_case


def get_one_final_case(a_string, index_list, one_case):
    """
    組合一個 case 的最終版，有以下步驟
    1. 從頭 (index: 0) 找到首個非英文的位置，先把非英文的部分篩選出來
    2. 依序從 index_list 裡面的 index_tuple 來篩選 one_case 裡的英文字母
       準備 append 到輸出字串 (one_final_case) 裡
    3. 因為 one_case 裡面應被篩選字母的 index 與原字串的 index 有差異
       這個位置差異是非英文字母的數量 (none_letter_number)
       所以在迴圈中會逐步計算 none_letter_number 的數量
    """
    one_final_case = ""
    none_letter_number = 0
    start_index = 0
    for index in index_list:
        one_final_case += a_string[start_index : index[0]]
        none_letter_number += index[0] - start_index
        one_final_case += one_case[index[0] - none_letter_number : index[1] - none_letter_number]
        start_index = index[1]
    one_final_case += a_string[index[1] :]
    return one_final_case


def final_function(a_string):
    """
    解題步驟
    1. 取得字串的小寫 case
    2. 取得字串裡面所有英文字母的位置，與其內容
    3. 取得 2. 步驟裡面英文字母的所有大小寫組合，以 list 收集
    4. 迴圈式針對這些英文字母大小寫 case 與原字串組合
    """
    a_string = a_string.lower()
    index_list, match_list = get_all_alphabeta(a_string)
    total_cases_list = get_all_case_for_string("".join(match_list))
    output = []
    for one_case in total_cases_list:
        output.append(get_one_final_case(a_string, index_list, one_case))
    return output


class Solution:
    """
    @param s: a string
    @return: return a list of strings
             we will sort your return value in output
    """

    def letter_case_permutation(self, s: str) -> List[str]:
        # write your code here
        if not re.search("\D+", s):
            return [s]
        return final_function(s)
