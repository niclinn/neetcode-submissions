# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groupPrev = dummy = ListNode(0, head)

        while True: 
            kth = self.getKth(groupPrev, k)
            if not kth: 
                break
            
            prev, curr = kth.next, groupPrev.next
            groupNext = kth.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next

    def getKth(self, head, k): 
        while head and k > 0: 
            head = head.next
            k -= 1
        return head