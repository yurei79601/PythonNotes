"""
把羅馬字母轉換成數字
我的核心概念：
1. 基本上就是把全部的字母翻譯成數字，加起來
2. 由左至右數，基本上數字會越來越小，如果下一個數字比較大那代表現在這個數字應該代表負值
"""
ROMAN_NUMBER_DICT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def main(a_string):
    number = 0
    for i, letter in enumerate(a_string):
        if i < len(a_string) - 1:
            if ROMAN_NUMBER_DICT[letter] >= ROMAN_NUMBER_DICT[a_string[i + 1]]:
                number += ROMAN_NUMBER_DICT[letter]
            else:
                number -= ROMAN_NUMBER_DICT[letter]
        else:
            number += ROMAN_NUMBER_DICT[letter]
    return number


class Solution:
    def romanToInt(self, s: str) -> int:
        return main(s)