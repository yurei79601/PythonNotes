"""
計算 excel 第 n 個欄位，名稱為何
"""
import string


number_to_map_1 = '-' + string.ascii_uppercase
number_to_map_0 = string.ascii_uppercase


def transform_to_digitals(input_number, digital_number):
    """
    將數字 (input_number) 轉換成 n (digital_number) 進位表示
    """
    digital_list = []
    quotient = input_number
    while quotient >= digital_number:
        remainder = quotient % digital_number
        quotient = quotient // digital_number
        digital_list.append(remainder)
    digital_list.append(quotient)
    return digital_list[::-1]


def map_alphabets(digital_list):
    """
    使用英文對照，要將 n 進位表示法轉換成英文字母
    註：因為個位數字的 A 當 0；但十位數字之後，A 就變成 1，
       所以兩個地方的對應會不同
    """
    alphabets_list = []
    for i, number in enumerate(digital_list):
        if i < len(digital_list) - 1:
            alphabets_list.append(number_to_map_1[number])
        else:
            alphabets_list.append(number_to_map_0[number])
    return alphabets_list


def get_excel_col(input_number):
    """
    將 input_number 轉為 excel 欄位代號
    因為個位數字的 A 是 0，所以會將數字減 1 再進行運算
    """
    digital_number = len(string.ascii_uppercase)
    digital_list = transform_to_digitals(input_number - 1, digital_number)
    alphabets_list = map_alphabets(digital_list)
    return ''.join(alphabets_list)


class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convert_to_title(self, n: int) -> str:
        # write your code here
        return get_excel_col(n)
