# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        number_1 = 0
        number_2 = 0
        curr = l1
        while curr:
            number_1 += multiplier * curr.val
            multiplier *= 10
            curr = curr.next
            
        
        multiplier = 1
        curr = l2
        while curr:
            number_2 += multiplier * curr.val
            multiplier *= 10
            curr = curr.next
        
        final = str(number_1 + number_2)[::-1]
        node = ListNode()
        node.val = final[0]
        dummy = node
        for i in range(len(final) - 1):
            if i + 1 != len(final):
                node.next = ListNode(val = final[i+1])
            node = node.next

        return dummy

        