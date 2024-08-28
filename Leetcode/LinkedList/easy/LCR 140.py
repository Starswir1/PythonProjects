head = [2, 4, 7, 8]
cnt = 1
a = len(head) - cnt


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.head = None

    def trainingPlan(self, head, cnt):
        """
        :type head: Optional[ListNode]
        :type cnt: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
