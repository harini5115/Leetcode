# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1, cur2 = headA, headB
        while cur1!=cur2:
            cur1 = headB if not cur1 else cur1.next
            cur2 = headA if not cur2 else cur2.next
        return cur1
        