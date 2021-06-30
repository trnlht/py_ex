from linked_list_tools import Node
from collections import defaultdict


def remove_duplicates(head):
    if head == None:
        return head

    prev = head
    cur = head.next
    elem_counters = defaultdict(int)
    elem_counters[prev.data] += 1

    while cur.next:
        elem_counters[cur.data] += 1
        if elem_counters[cur.data] > 1:
            prev.next = cur.next
        else:
            prev = prev.next

        cur = cur.next

