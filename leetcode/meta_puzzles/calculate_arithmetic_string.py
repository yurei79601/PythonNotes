"""
給定一個字串，內容僅包含加法與乘法的敘述，製造出一個函數，可以計算這個字串的結果
[ex1]

input: "3 * 5 + 1"
returs: 16

[ex2]

input: "4 * 2 + 9 * 5 + 2 * 6 * 3"
return: 89
"""


def function(a_string: str) -> int:
    """
    decode arithmetic statement and return the result of calculation
    """
    multiplication_part = [part.replace(' ', '') for part in a_string.split('+')]  # O(addition_numbers)
    multiplication_splits = [
        splits.split('*') for splits in multiplication_part
    ]  # O(muplication_numbers)
    _sum = 0
    for splits in multiplication_splits:  # O(muplication_numbers)
        one_multiplication_result = 1
        for string_number in splits:  # O(muplication_numbers - 1)
            one_multiplication_result *= int(string_number)
        _sum += one_multiplication_result
    return _sum
