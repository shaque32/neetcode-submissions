# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

      
        cur = head
        stack = []

        while cur:
            stack.append(cur)
            cur = cur.next
        first = head
        for _ in range(len(stack)//2):
            last = stack.pop()
            nextFirst = first.next
            first.next = last
            last.next = nextFirst

            first = nextFirst
        first.next = None
        
        


