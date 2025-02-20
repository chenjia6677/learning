# 排序算法
from typing import List


class MergeSort:
    """
    归并排序算法
    """
    @staticmethod
    def merge(left: list, right: list) -> list:
        """
        对2个已经排序的数组进行归并
        """
        result = list()

        while left or right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

            if not (left and right):
                break

        return result + left + right

    def merge_sort(self, data: list) -> list:
        """
        排序
        """
        element_number = len(data)  # 元素数量

        if element_number < 2:  # 基本条件
            return data

        # 划分
        left_data = data[: element_number // 2]
        right_data = data[element_number // 2:]

        return self.merge(self.merge_sort(left_data), self.merge_sort(right_data))


class TournamentSort:
    """
    锦标赛排序
    假设有一个包含n个不同的数的未排序数据，其中 n 是 2 的整数次方。提供一种算法，确认数组中第二大的数，最多只能使用 n + log2n - 2次比较
    参考资料：https://www.cnblogs.com/james1207/p/3323115.html
    """

    def main(self, arr: List[int]) -> int:
        max_value, comparisons = self.build_tournament_tree(arr)
        candidates = set()

        # 找到与最大值直接比较过的元素
        for a, b, winner in comparisons:
            if winner == max_value:
                candidates.add(a if a != max_value else b)

        # 在候选元素中找到第二大的数
        second_max = max(candidates)
        return second_max

    @staticmethod
    def build_tournament_tree(arr: List[int]) -> tuple:
        """
        构造淘汰赛树 / 锦标赛树
        """
        n = len(arr)
        tree = arr.copy()  # 初始化叶子节点
        comparisons = []  # 记录比较路径

        while n > 1:
            new_level = []
            for i in range(0, n, 2):
                if i + 1 < n:
                    winner = max(tree[i], tree[i + 1])
                    comparisons.append((tree[i], tree[i + 1], winner))
                    new_level.append(winner)
                else:
                    new_level.append(tree[i])
            tree = new_level
            n = len(tree)

        return tree[0], comparisons


if __name__ == '__main__':
    # m = MergeSort()
    # # r = m.merge([1, 4, 5, 8], [2, 3, 6, 7, 9])
    # r = m.merge_sort([5, 4, 1, 8, 7, 2, 6, 3, 9])
    # print(r)

    t = TournamentSort()
    x = t.main([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print(x)









