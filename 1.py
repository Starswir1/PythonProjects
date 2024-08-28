# from datetime import datetime, timedelta
#
# words = ["one.two.three", "four.five", "six"]
# print(str(words))
# a = range(1, 11, 1)
# print(a)
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """在链表末尾添加一个新节点"""
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def prepend(self, value):
        """在链表开头添加一个新节点"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """删除链表中第一个值为指定值的节点"""
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_list(self):
        """打印链表中的所有值"""
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()


# 示例用法
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.print_list()  # 输出: 0 1 2 3
ll.delete(2)
ll.print_list()  # 输出: 0 1 3
