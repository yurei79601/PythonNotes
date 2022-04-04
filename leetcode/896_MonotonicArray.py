from typing import List


def check_increase(a: float, b: float) -> bool:
    return a > b


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(set(nums)) <= 1:
            return True

        monotone_way_dict = {}

        for i in range(len(nums) - 1):
            a = nums[i]
            b = nums[i + 1]

            if a != b:
                monotone_way = check_increase(b, a)
                monotone_way_dict.update({monotone_way: 1})

            if len(monotone_way_dict.keys()) > 1:
                return False

        return True