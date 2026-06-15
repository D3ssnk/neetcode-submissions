# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split in half
        slowp = head
        fastp = head.next
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next

        # reverse second half
        curr = slowp.next
        prev = slowp.next = None     
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        node = prev
        while node:
            temp1 = head.next
            temp2 = node.next
            head.next = node
            node.next = temp1
            head = temp1 
            node = temp2
        


        