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
