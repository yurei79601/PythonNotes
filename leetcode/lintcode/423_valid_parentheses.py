"""
確認一個字串裡面的括號表示是否合理
"""


check_list = ['()', '[]', '{}']


def remove_valid_parentheses(a_string):
    """
    去除字串裡的 "合規字串"
    """
    for parentheses in check_list:
        if parentheses in a_string:
            return a_string.replace(parentheses, "")
    return a_string


def main(a_string):
    """
    確認字串的括號是否合規
    [idea] 不斷刪除字串裡頭合規的括號
        1. 若可以將字串刪除成為空字串，表示裡頭全部皆合規
        2. 若在某一個步驟，有刪除與沒刪除相同，則不合規
    """
    while a_string:
        b_string = remove_valid_parentheses(a_string)
        if b_string == "":
            return True
        if a_string == b_string:
            return False
        a_string = b_string

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        return main(s)
