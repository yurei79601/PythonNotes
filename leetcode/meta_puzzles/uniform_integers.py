"""
A positive integer is considered uniform if all of its digits are equal. For example, 222 is uniform, while 223 is not.
Given two positive integers A and B, determine the number of uniform integers between A and B, inclusive.
Please take care to write a solution which runs within the time limit.

簡言之，找出介於 A (小) 與 B (大) 之間的 uniform integers
"""


def count_uniform_integers(number: int) -> int:
    """
    計算從 0 ~ number 之間的 uniform integers 有多少
    [idea]
    因為 uniform integers 一定都是 11...1 的倍數，所以就用除法來解
    第 N 位數的數字是否為 uniform integers 就是除以 N 位數的 1 來看商數
    又因為 N - 1 位數的 uniform integers 也比 number 還要小，
    當然 N - 2 位數也是，所以就一直這樣加到第 1 位數
    每種位數裡的 uniform integers 有 9 個，因此公式如下
    """
    digitals = len(str(number))
    base = int('1' * digitals)
    return number // base + 9 * (digitals - 1)


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    """
    meta 的測驗的主函數
    """
    return count_uniform_integers(B) - count_uniform_integers(A - 1)
