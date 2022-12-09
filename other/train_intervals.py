import unittest

"""
Даны N файлов (списков). Каждый представляет собой набор временных меток для одного пути на станции, 
причем нечетный номер строки (элемента) - прибытие поезда, четный - убытие. Необходимо найти временные интервалы,
в которые все N путей на станции были заняты. 
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

    # Размечаем списки и объединяем их в один список
    for log_list in log_lists:
        marked_log_list = get_marked_log_list(log_list)
        general_marked_log_list.extend(marked_log_list)

    # Сортируем общий список по меткам времени
    general_marked_log_list.sort(key=lambda item: item[0])

    intervals = []
    train_counter = 0   # Счетчик поездов
    start = 0

    for item in general_marked_log_list:
        if item[1] == "a":
            train_counter += 1
        else:
            train_counter -= 1

        # Если все пути заняты - фиксируем начальную метку
        if train_counter == N:
            start = item[0]
        else:
            # Если не все и отсчет был начат то фиксируем конечную метку и обнуляем старт
            if start:
                intervals.append((start, item[0]))
                start = 0

    return intervals


def get_marked_log_list(log_list):
    """
    Маркирует список временных меток. Нечетные элементы - прибытие, четные - отправление
    :param log_list: Список временных меток
    :return: Маркированный список кортежей (временная метка, тип)
    """
    marked_log_list = []
    num = 1
    for i in range(len(log_list)):
        marked_log_list.append((log_list[i], "a" if (num % 2) != 0 else "d"))
        num += 1

    return marked_log_list


class GetIntervalsTester(unittest.TestCase):
    def test_should_return_correct_intervals(self):
        self.assertEqual(get_intervals([[5, 10, 15, 20], [7, 12, 17, 23]]), [(7, 10), (17, 20)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
