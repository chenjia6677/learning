from tools import timer

"""
题目：
假设农场中成熟的母牛每年都会生 1 头小母牛，并且永远不会死。
第 1 年有 1 只即将成熟的母牛， 从第 2 年开始生小母牛。
每只小母牛 3 年之后成熟又可以生小母牛。
给定整数 N， 求 N 年后牛的数量

分析：
第 1  年牛的数量是 1   (注：因为第 1 年只有 1 只即将成熟的母牛， 从第 2 年开始生小母牛）
第 2  年牛的数量是 2   (注：仅有的 1 只成熟母牛生了 1 只小母牛）
第 3  年牛的数量是 3   (注：仅有的 1 只成熟母牛生了 1 只小母牛）
第 4  年牛的数量是 4   (注：仅有的 1 只成熟母牛生了 1 只小母牛）
第 5  年牛的数量是 6   (注：第 2  年出生的小母牛成熟了，仅有的 2  只成熟母牛生了 2  只小母牛）
第 6  年牛的数量是 9   (注：第 3  年出生的小母牛成熟了，仅有的 3  只成熟母牛生了 3  只小母牛）
第 7  年牛的数量是 13  (注：第 4  年出生的小母牛成熟了，仅有的 4  只成熟母牛生了 4  只小母牛）
第 8  年牛的数量是 19  (注：第 5  年出生的小母牛成熟了，仅有的 6  只成熟母牛生了 6  只小母牛）
第 9  年牛的数量是 28  (注：第 6  年出生的小母牛成熟了，仅有的 9  只成熟母牛生了 9  只小母牛）
第 10 年牛的数量是 41  (注：第 7  年出生的小母牛成熟了，仅有的 13 只成熟母牛生了 13 只小母牛）
第 11 年牛的数量是 60  (注：第 8  年出生的小母牛成熟了，仅有的 19 只成熟母牛生了 19 只小母牛）
第 12 年牛的数量是 88  (注：第 9  年出生的小母牛成熟了，仅有的 28 只成熟母牛生了 28 只小母牛）
第 13 年牛的数量是 129 (注：第 10 年出生的小母牛成熟了，仅有的 41 只成熟母牛生了 41 只小母牛）
第 14 年牛的数量是 189 (注：第 11 年出生的小母牛成熟了，仅有的 60 只成熟母牛生了 60 只小母牛）
第 15 年牛的数量是 277 (注：第 12 年出生的小母牛成熟了，仅有的 88 只成熟母牛生了 88 只小母牛）

dp[15] = dp[14] + dp[12]
dp[i] = dp[i-1] + dp[i-3]
"""


class CowCalve(object):

    @staticmethod
    @timer
    def dynamic_programming(n: int) -> int:
        """
        动态规划法
        :param n: 第 N 年
        :return: 第 N 年牛的数量
        """

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 3]

        return dp[n]

    @staticmethod
    @timer
    def optimize_dp(n: int) -> int:
        """
        动态规划法空间优化版
        :param n: 第 N 年
        :return: 第 N 年牛的数量
        """
        a, b, c = 1, 2, 3

        for i in range(4, n + 1):
            a, b, c = b, c, a + c

        return c

    def recursive(self, n: int) -> int:
        """
        递归法
        :param n: 第 N 年
        :return: 第 N 年牛的数量
        """
        if n <= 4:
            return n

        return self.recursive(n - 1) + self.recursive(n - 3)

    @timer
    def test_recursive(self, n):
        return self.recursive(n)

    def test(self, n: int):
        """
        :param n: 第 N 年
        :return: 第 N 年牛的数量
        """
        return self.dynamic_programming(n), self.optimize_dp(n), self.test_recursive(n)


if __name__ == '__main__':
    cc = CowCalve()
    print(cc.test(35))