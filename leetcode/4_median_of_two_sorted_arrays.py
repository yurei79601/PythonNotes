def sort_list(a_list, reverse=False):
    for i in range(len(a_list)-1):
        for j in range(i, len(a_list)-1):
            a = a_list[i]
            b = a_list[j+1]
            if a > b:
                a_list[i] = b
                a_list[j+1] = a

                a = a_list[i]
                b = a_list[j+1]
    if reverse:
        return a_list[::-1]
    return a_list


def get_median(a_list):
    if len(a_list) % 2 != 0:
        median_index = int((len(a_list) - 1)/2)
        return a_list[median_index]
    first_index = int(len(a_list)/2)
    second_index = int((len(a_list)/2) - 1)
    return (a_list[first_index] + a_list[second_index]) / 2


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a_list = nums1 + nums2
        sorted_list = sort_list(a_list)
        return get_median(sorted_list)
        