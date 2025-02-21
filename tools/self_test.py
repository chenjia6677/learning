from typing import List

from tools import timer


class FunctionTest(object):
    """
    功能测试
    """
    def __init__(self, instance):
        """
        :instance: 实例
        """
        self.instance = instance
        self.cases = []  # 测试用例

    def test(self, methods: List[str], num: int):
        """
        :param methods: 待测试的方法
        :param num: 参数数量
        """
        for method in methods:
            if not hasattr(type(self.instance), method):
                continue

            func = getattr(self.instance, method)  # 待测试的方法

            for case in self.cases:  # 测试用例

                param = case[num] if num == 1 else case[1: num + 1]  # 参数

                result = case[num + 1:]
                expected_result = result[0] if len(result) else tuple(result)  # 预期结果

                actual_result = func(param)  # 实际结果

                if expected_result != actual_result:
                    print(f'{func.__name__} 方法的预期结果是 {expected_result}，实际结果是 {actual_result}；测试用例是 {case}')

        print('功能测试结束！！！')


class PerformanceTest(FunctionTest):
    @staticmethod
    @timer
    def performance(method, param):
        """
        :param method: 待测试的方法
        :param param: 参数
        """
        return method(param)

    def test(self, methods: List[str], num: int):
        """
        :param methods: 待测试的方法
        :param num: 参数数量
        """
        for method in methods:
            if not hasattr(type(self.instance), method):
                continue

            func = getattr(self.instance, method)  # 待测试的方法

            for case in self.cases:  # 测试用例
                param = case[num] if num == 1 else case[1: num + 1]  # 参数
                cost = self.performance(func, param)[-1]  # 性能测试
                print(f'{func.__name__} 方法的测试用例是 {case}, 耗时 {cost} 毫秒')

        print('性能测试结束！！！')

