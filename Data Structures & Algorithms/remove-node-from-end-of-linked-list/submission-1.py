# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        fast = dummy
        prev = None


        for i in range(n):
            fast = fast.next

        
        while fast.next:
            cur = cur.next
            fast = fast.next
        
        cur.next = cur.next.next

        return dummy.next
        