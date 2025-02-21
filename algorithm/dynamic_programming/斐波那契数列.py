from tools import FunctionTest, PerformanceTest


class FibonacciSequence(object):
    """
    斐波那契数列
    """
    @staticmethod
    def common(index: int) -> int:
        """
        计算第n个斐波那契数（普通法）
        :param index: 第index个斐波那契数（从0开始计数，第0个数是0，第1个数是1）
        :return: 斐波那契数
        """
        a, b = 0, 1

        num = 0
        while num < index:
            a, b = b, a + b
            num += 1

        return a

    @staticmethod
    def recursive(index: int) -> int:
        """
        计算第n个斐波那契数（递归法）
        :param index: 第index个斐波那契数（从0开始计数，第0个数是0，第1个数是1）
        :return: 斐波那契数
        """
        if index <= 1:
            return index

        return FibonacciSequence.recursive(index - 1) + FibonacciSequence.recursive(index - 2)

    @staticmethod
    def dynamic_programming(index: int) -> int:
        """
        计算第n个斐波那契数（动态规划法）
        :param index: 第index个斐波那契数（从0开始计数，第0个数是0，第1个数是1）
        :return: 斐波那契数
        """
        if index <= 1:
            return index

        dp = [0] * (index + 1)
        dp[1] = 1
        for i in range(2, index + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[index]


if __name__ == '__main__':
    fs = FibonacciSequence()

    # 功能测试
    ft = FunctionTest(fs)
    ft.cases = [
            ['基础边界条件-初始条件', 0, 0],
            ['基础边界条件-初始条件', 1, 1],
            ['小数值验证-简单递推', 2, 1],
            ['小数值验证-典型计算', 5, 5],
            ['小数值验证-中等计算', 10, 55],
            ['中等数值验证-递推验证', 20, 6765],
            ['中等数值验证-大数计算', 30, 832040]
        ]
    ft.test(['common', 'recursive', 'dynamic_programming'], 1)

    # 性能测试
    pt = PerformanceTest(fs)
    pt.cases = [
            ['递归算法性能-指数爆炸', 35, 9227465],
            ['递归算法性能-不可行性', 40, 102334155],
            ['动态规划/迭代算法性能-线性时间', 100, 354224848179261915075],
            ['动态规划/迭代算法性能-大数处理', 1000, '末4位 6865'],
            ['动态规划/迭代算法性能-超大规模', 1000000, '末4位 6875']
        ]
    pt.test(['common', 'dynamic_programming'], 1)

    """
    common 方法的测试用例是 ['递归算法性能-指数爆炸', 35, 9227465], 耗时 0.00  毫秒
    common 方法的测试用例是 ['递归算法性能-不可行性', 40, 102334155], 耗时 0.00  毫秒
    common 方法的测试用例是 ['动态规划/迭代算法性能-线性时间', 100, 354224848179261915075], 耗时 0.00  毫秒
    common 方法的测试用例是 ['动态规划/迭代算法性能-大数处理', 1000, '末4位 6865'], 耗时 0.00  毫秒
    common 方法的测试用例是 ['动态规划/迭代算法性能-超大规模', 1000000, '末4位 6875'], 耗时 5799.93  毫秒
    recursive 方法的测试用例是 ['递归算法性能-指数爆炸', 35, 9227465], 耗时 1209.47  毫秒
    recursive 方法的测试用例是 ['递归算法性能-不可行性', 40, 102334155], 耗时 13528.35  毫秒
    recursive 方法的测试用例是 ['动态规划/迭代算法性能-线性时间', 100, 354224848179261915075], 很久...
    recursive 方法的测试用例是 ['动态规划/迭代算法性能-大数处理', 1000, '末4位 6865'], 很久...
    recursive 方法的测试用例是 ['动态规划/迭代算法性能-超大规模', 1000000, '末4位 6875'], 很久...
    dynamic_programming 方法的测试用例是 ['递归算法性能-指数爆炸', 35, 9227465], 耗时 0.00  毫秒
    dynamic_programming 方法的测试用例是 ['递归算法性能-不可行性', 40, 102334155], 耗时 0.00  毫秒
    dynamic_programming 方法的测试用例是 ['动态规划/迭代算法性能-线性时间', 100, 354224848179261915075], 耗时 0.00  毫秒
    dynamic_programming 方法的测试用例是 ['动态规划/迭代算法性能-大数处理', 1000, '末4位 6865'], 耗时 0.00  毫秒
    dynamic_programming 方法的测试用例是 ['动态规划/迭代算法性能-超大规模', 1000000, '末4位 6875'], 很久...
    """
