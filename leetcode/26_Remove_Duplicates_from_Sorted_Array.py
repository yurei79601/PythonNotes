"""
create a function with the property
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
f(nums) = 5
and nums = [0, 1, 2, 3, 4] eventually
"""
from typing import List


# submit function
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# my function but failed
def main(nums):
    distinct_number = 1
    look_forward_number = 1
    while len(nums) > distinct_number:
        print(distinct_number, look_forward_number, nums)
        if nums[distinct_number - 1] == nums[distinct_number - 1 + look_forward_number]:
            look_forward_number += 1
        else:
            nums = nums[:distinct_number] + nums[distinct_number - 1 + look_forward_number:]
            print(f"nums[:{distinct_number}] + nums[{look_forward_number}:]")
            distinct_number += 1
            look_forward_number = 1
    return len(nums)
