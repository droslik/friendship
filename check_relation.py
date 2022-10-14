from collections import deque


def check_relation(net, first, second):
    graph = {}
    list_names = []
    for pair in net:
        for name in pair:
            if name not in list_names:
                list_names.append(name)
    for name in list_names:
        graph[name] = []
        for net_pair in net:
            if name in net_pair:
                graph[name].append(net_pair[0] if net_pair[0] != name else net_pair[1])
    checked = [first, ]
    first_queue = deque()
    second_queue = deque()
    if first in graph[second]:
        return True
    checked.append(second)
    first_queue += graph[first]
    second_queue += graph[second]
    while first_queue:
        checking_name = first_queue.popleft()
        if checking_name in second_queue:
            return True
        else:
            checked.append(checking_name)
            for name in graph[checking_name]:
                if name not in checked and name not in first_queue:
                    first_queue.append(name)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Леша"), ("Леша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Леша", "Лена"), ("Оля", "Петя"),
        ("Степа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Леша", "Настя") is False
    assert check_relation(net, "Степа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True

