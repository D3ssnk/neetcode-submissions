# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        countp = head
        count = 0 
        while countp:
            countp = countp.next
            count += 1
        
        location = count - n

        if location == 0: return head.next
        curr = head
        while location != 1:
            curr = curr.next
            location -= 1
        
        second = curr.next.next
        curr.next = second




        return head