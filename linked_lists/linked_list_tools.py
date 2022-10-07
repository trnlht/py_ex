from dataclasses import dataclass

import unittest

# @dataclass
# class Node:
    # data: int
    # next: Node

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def create_linked_list_from_list(input_list):
    if not input_list:
        return None

    head = Node(data=input_list[0], next=None)
    cur = head

    for val in input_list[1:]:
        new_node = Node(val, None)
        cur.next = new_node
        cur = new_node

    return head

def traverse(head):
    cur = head
    while cur != None:
        yield cur
        cur = cur.next

def check_linked_list_and_list_equal(linked_list, list):
    pass



class CreateLinkedListFromListTester(unittest.TestCase):
    def test_create_empty_linked_list_from_list(self):
        self.assertEqual(None, create_linked_list_from_list([]))
    
    def test_create_linked_list_from_list(self):
        input_lists = [[1], [1,2,3], [1,2,3,4,5], [0, 0, 0, 0]]

        for input_list in input_lists:
            head = create_linked_list_from_list(input_list)
            i = 0
            cur = head
            while cur != None:
                self.assertEqual(cur.data, input_list[i])
                cur = cur.next
                i += 1

class TraverseTester(unittest.TestCase):
    def test_traverse_empty_list(self):
        head = create_linked_list_from_list([])

        gen = traverse(head)

        self.assertRaises(StopIteration, next, gen)

    def test_traverse_list(self):
        input_list = [1, 2, 3]
        head = create_linked_list_from_list(input_list)

        for node, val in zip(traverse(head), input_list):
            self.assertEqual(node.data, val)

        i = 0
        for node in traverse(head):
            self.assertEqual(node.data, input_list[i])
            i += 1



        

if __name__ == "__main__":
    unittest.main(verbosity=2)
