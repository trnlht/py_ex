import unittest

"""
Odd line number is arrival, even is departure
log_list_1:
5
10
15
20

log_list_2:
7
12
17
23
"""

def get_intervals(log_lists):
    N = len(log_lists)
    general_marked_log_list = []

    for log_list in log_lists:
        marked_log_list = get_marked_log_list(log_list)
        general_marked_log_list.extend(marked_log_list)
        
    general_marked_log_list.sort(key=lambda item: item[0])

    intervals = []
    train_counter = 0
    start = 0

    for item in general_marked_log_list:
        if item[1] == "a":
            train_counter += 1
        else:
            train_counter -= 1

        if train_counter == N:
            start = item[0]
        else:
            if start:
                intervals.append((start, item[0]))
                start = 0

    return intervals


def get_marked_log_list(log_list):
    marked_log_list = []
    num = 1
    for i in range(len(log_list)):
        marked_log_list.append((log_list[i], "a" if (num % 2) != 0 else "d"))
        num += 1

    return marked_log_list



class GetIntervalsTester(unittest.TestCase):
    def test_should_return_correct_intervals(self):
        self.assertEqual(get_intervals([[5, 10, 15, 20],[7, 12, 17, 23]]), [(7, 10), (17, 20)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
