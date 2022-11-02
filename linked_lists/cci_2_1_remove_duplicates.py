import unittest
from linked_list_tools import Node, create_linked_list_from_list, traverse
from collections import defaultdict


def remove_duplicates(head: Node):
    """
    Removes duplicates from linked list.
    Complexity: O(N)
    [CCI 2.1]

    :param head: Original list
    """
    if head == None:
        return head

    s = set()
    s.add(head.data)
    
    cur = head

    while cur.next != None:
        if cur.next.data in s:
            cur.next = cur.next.next
        else:
            s.add(cur.next.data)
            cur = cur.next

    return head

class RemoveDuplicatesTester(unittest.TestCase):

    def test_remove_duplicates_from_empty_list(self):
        head = None
        self.assertEqual(remove_duplicates(head), None)

    def test_remove_duplicates_from_list(self):
        head = create_linked_list_from_list([0])

        new_head = remove_duplicates(head)

        expected_list = [0]
        for node, val in zip(traverse(new_head), expected_list, strict=True):
            self.assertEqual(node.data, val)


if __name__ == "__main__":
    unittest.main(verbosity=2)

    # prev = head
    # cur = head.next
    # elem_counters = defaultdict(int)
    # elem_counters[prev.data] += 1

    # while cur.next:
        # elem_counters[cur.data] += 1
        # if elem_counters[cur.data] > 1:
            # prev.next = cur.next
        # else:
            # prev = prev.next

        # cur = cur.next

