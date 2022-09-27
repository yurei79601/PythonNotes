"""
use node to construct a function with the following logic:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
"""
from typing import Optional


class ListNode:
    """
    Definition for singly-linked list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def extract_values_from_node(a_list: ListNode) -> list:
    """
    從 ListNode 將整串值拿出來
    """
    value_list = []
    if not a_list:
        return value_list

    while True:
        value = getattr(a_list, 'val')
        value_list.append(value)
        a_list = getattr(a_list, 'next')
        if not a_list:
            break
    return value_list


def transform_node_to_list(output_list: list) -> ListNode:
    """
    將 list 裡面的值，照順序組成 ListNode
    概念：從最後一個 value 開始建立 ListNode，接著再一層一層取代
    """
    output_node = ListNode(val=None, next=None)
    if not output_list:
        return
    for i, val in enumerate(output_list[::-1]):
        if not i:
            a_node = ListNode(
                val=val
            )
        else:
            a_node = ListNode(
                val=val,
                next=output_node
            )
        output_node = a_node
    return output_node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        想法：
        1. 因為操作 ListNode 不易，所以都先轉成各自的 list value
        2. 將兩個 list value 合併，並且排序
        3. 再將這個 list value 組成 ListNode
        """
        value_list1 = extract_values_from_node(list1)
        value_list2 = extract_values_from_node(list2)
        value_list1.extend(value_list2)
        output_list = sorted(value_list1)
        if not output_list:
            return None
        output_node = transform_node_to_list(output_list)
        return output_node
