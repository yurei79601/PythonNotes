# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.b = 2

    def GetListNode(self, a_list):
        d = {}
        if len(a_list) == 1:
            return ListNode(a_list[0])
        for i in range(len(a_list)-1):
            a = ListNode(a_list[i])
            a.next = ListNode(a_list[i+1])
            d[i] = a
        reverse_a_list = a_list[::-1]
        for i in range(len(reverse_a_list)-2):
            d[i].next = d[i+1]
        return d[0]
    
    def node_to_list(self, a):
        decode_list = [a.val]
        #print(a.val)
        while True:
            #print(a.next.val)
            if a.next == None:
                break
            decode_list.append(a.next.val)
            a = a.next
        return decode_list
    
    def decode_values(self, listnode):
        #listnode = self.GetListNode(a_list)
        a_list = self.node_to_list(listnode)
        list_num = 0
        for i, x in enumerate(a_list):
            list_num += x * (10 ** i)
        return list_num
    
    def number_to_list(self, a_number):
        a_list = [int(x) for x in list(str(a_number))]
        return a_list[::-1]
    
    def addTwoNumbers(self, l1, l2):
        l3_num = self.number_to_list(self.decode_values(l1) + self.decode_values(l2))
        return self.GetListNode(l3_num)
