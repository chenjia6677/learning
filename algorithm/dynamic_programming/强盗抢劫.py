from tools import timer

from typing import List


"""
题目：
抢劫一排住户，但是不能抢邻近的住户，求最大抢劫量

分析：
定义一个数组 dp 存储最大抢劫量，dp[i] 表示抢到第 i 个住户时的最大抢劫量。
因为不能抢劫邻近的住户，所以如果抢劫了第 i-1 个住户，那么就不能抢劫第 i 个住户，
即：dp[i] = max(dp[i-2] + nums[i], dp[i-1])

分析:
nums = [2, 7, 9, 3, 1]
一排有 1 个住户，最大抢劫量是 2 （注：抢第 1 个住户）
一排有 2 个住户，最大抢劫量是 7 （注：抢第 2 个住户）
一排有 3 个住户，最大抢劫量是 11（注：抢第 1和3 个住户）
一排有 4 个住户，最大抢劫量是 11（注：抢第 1和3 个住户）
一排有 5 个住户，最大抢劫量是 12（注：抢第 1和3和5 个住户）
"""


class HouseRobber(object):

    @staticmethod
    @timer
    def dynamic_programming(nums: List[int]) -> int:
        """
        动态规划法
        :param nums: 每个住户可被抢劫的量
        :return: 最大抢劫量
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    @staticmethod
    @timer
    def optimize_dp(nums: List[int]) -> int:
        """
        动态规划法空间优化版
        :param nums: 每个住户可被抢劫的量
        :return: 最大抢劫量
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        a = nums[0]
        b = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(a + nums[i], b)

        return b

    def recursive(self, nums: List[int]) -> int:
        """
        动态规划法空间优化版
        :param nums: 每个住户可被抢劫的量
        :return: 最大抢劫量
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.recursive(nums[: -2]) + nums[-1], self.recursive(nums[: -1]))

    @timer
    def test_recursive(self, n):
        return self.recursive(n)

    def test(self, nums: List[int]):
        """
        :param nums: 每个住户可被抢劫的量
        :return: 最大抢劫量
        """
        return self.dynamic_programming(nums), self.optimize_dp(nums), self.test_recursive(nums)


if __name__ == '__main__':
    hr = HouseRobber()
    print(hr.test([2, 7, 9, 3, 1, 2, 7, 9, 3, 1, 2, 7, 9, 3, 1, 2, 7, 9, 3, 1, 2, 7, 9, 3, 1, 2, 7, 9, 3, 1]))



