# @before-stub-for-debug-begin
from python3problem707 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if (index >= self.size or index < 0):  # list index out of range or index negative
            return - 1

        temp = self.head
        for _ in range(index):
            temp = temp.next

        # self.printList()  # For debug
        # print(f"\ndone get {index}\n")  # For debug
        # print("-----------------------------------") # For debug
        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        new_node = Node(val)
        if (self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1
        # self.printList()  # For debug
        # print(f"\ndone addAtHead {val}\n")  # For debug
        # print("-----------------------------------") # For debug

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        new_node = Node(val)
        if (self.head == None):
            self.head = new_node

        else:
            temp = self.head
            while (temp):
                prev = temp
                temp = temp.next
            prev.next = new_node

        self.size += 1
        # self.printList()  # For debug
        # print(f"\ndone addAtTail {val}\n")  # For debug
        # print("-----------------------------------")

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if (self.head == None):
            self.head = Node(val)

        elif (index == 0):
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

        else:
            temp = self.head
            for _ in range(index):
                prev = temp
                temp = temp.next
            new_node = Node(val)
            prev.next = new_node
            new_node.next = temp

        self.size += 1
        # self.printList()  # For debug
        # print(f"\ndone addAtIndex [{index} {val}]\n")  # For debug
        # print("-----------------------------------")

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if (index >= self.size):  # list index out of range
            return -1

        elif (index == 0):  # head
            temp = self.head
            self.head = temp.next
            temp = None

        else:
            temp = self.head
            for _ in range(index):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp = None

        self.size -= 1
        # self.printList()  # For debug
        # print(f"\ndone deleteAtIndex {index}\n")  # For debug
        # print("-----------------------------------")

    # For debug
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val, end=" -> ")
            temp = temp.next
        print("\n")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
