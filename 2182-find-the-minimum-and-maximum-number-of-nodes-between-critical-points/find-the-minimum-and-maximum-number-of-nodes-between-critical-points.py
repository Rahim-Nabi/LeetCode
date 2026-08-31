# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_c = -1
        start_c = -1
        min_c = float('inf')

        prev = curr = head
        i = 0
        while curr.next:
            nexts = curr.next

            if prev.val < curr.val > nexts.val or prev.val > curr.val < nexts.val:
                if start_c == -1:
                    start_c = i
                if prev_c != -1:
                    min_c = min(min_c, i-prev_c)
                prev_c = i
            
            prev = curr
            curr = curr.next
            i += 1

        if min_c == float('inf'):
            return [-1,-1]
        return [min_c, prev_c - start_c]