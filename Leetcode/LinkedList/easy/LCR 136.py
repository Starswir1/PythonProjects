head = [4, 5, 1, 9]
node = 1


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')

    def deleteNode(self, node):
        dummy = ListNode(0)
        dummy.next = head
        prev = None
        cur = self.head

        while cur and cur.data != node:
            prev = cur
            cur = cur.next
        prev.next = cur.next


if __name__ == '__main__':
    s = Solution()

    # 删除值为 1 的节点
    s.deleteNode(node)
    s.print_list()
