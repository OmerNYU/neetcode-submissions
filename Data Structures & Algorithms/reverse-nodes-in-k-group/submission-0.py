# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, head:Optional[ListNode], group_next) -> Optional[ListNode]:
        
        curr = head
        prev = group_next

        while curr != group_next:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:

            kth = group_prev

            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            old_group_start = group_prev.next

            new_group_head = self.reverseGroup(old_group_start, group_next)

            group_prev.next = new_group_head
            group_prev = old_group_start