# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen_numbers = set()
        while curr and curr.val not in seen_numbers:
            seen_numbers.add(curr.val)
            curr = curr.next

         
        return True if curr else False

        