# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_p = dummy

        while True:
            kth = group_p
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
        
            groupNext = kth.next 

            prev, curr = groupNext, group_p.next
            while curr != groupNext:
                temp =  curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_p.next
            group_p.next = kth
            group_p = temp