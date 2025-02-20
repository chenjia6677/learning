from typing import List, Set, Any, Tuple


def nested_loop(source: List[Set[Any]], current: List[Any] = None, index: int = 0) -> List[Tuple[Any]]:
    """
    多层嵌套循环
    :param source: 源数据
    :param current: 当前分配情况
    :param index: 当前分配的位置
    :return: 所有可能的分配方案
    """
    if current is None:
        current = [None] * len(source)

    if index == len(source):  # 分配完毕
        return [tuple(current)]

    result = []
    for enum in source[index]:
        current[index] = enum
        result.extend(nested_loop(source, current, index + 1))

    return result


if __name__ == '__main__':
    source = [{'a', 'b'}, {1, 2}, {0.3, 0.4}]
    target = nested_loop(source)
    print(target)

