
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr != None:
            length += 1
            curr = curr.next


        targetIndex = (length - 1) - (n - 1)

        curr = head
        head = self.remove(head, targetIndex, length)
        return head

    def remove(self, head, targetIndex, length):
        curr = head
        '''
        3 cases to removal
        1. head
        2. middle
        3. tail
        '''
        if targetIndex == 0: # head
            head = head.next
            return head
        elif length - targetIndex >= 1: # middle
            for i in range(targetIndex - 1):
                curr = curr.next
            curr.next = curr.next.next
            return head
        else: # tail
            for i in range(length - 2):
                curr = curr.next
            curr.next = None
            return head