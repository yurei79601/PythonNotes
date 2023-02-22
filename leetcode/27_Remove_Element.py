"""
create a function with the property
nums = [0, 1, 2, 2, 3, 0, 4, 2]
f(nums) = 5
and nums = [0, 1, 3, 0, 4] eventually
"""
from typing import List


def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] != val:
            i += 1
        else:
            nums.pop(i)
    return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return remove_element(nums, val)
