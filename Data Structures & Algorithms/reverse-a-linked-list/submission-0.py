# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        curr = head

        while(curr):
            stack.append(curr)
            curr = curr.next

        endHead = stack.pop()
        curr = endHead

        while stack:
            node = stack.pop()  
            curr.next = node
            curr = node
        curr.next = None
        return endHead

                



        