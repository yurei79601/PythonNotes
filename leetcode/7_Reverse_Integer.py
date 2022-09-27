UPPER_BOUND = 2 ** 31 - 1
LOWER_BOUND = - 2 ** 31


def exceed_range(x):
    return x > UPPER_BOUND or x < LOWER_BOUND


class Solution:
    def reverse(self, x: int) -> int:
        if exceed_range(x):
            return 0
        sign = x < 0
        result = (-1) ** sign * int(str(abs(x))[::-1])
        if exceed_range(result):
            return 0
        return (-1) ** sign * int(str(abs(x))[::-1])
