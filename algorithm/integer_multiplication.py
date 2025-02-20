# 整数相乘算法

import math
import time
import random


class GradeSchool:
    """
    小学算法（只会个位数加法和乘法）
    """
    def __init__(self):
        # 个位数加法表
        self.addition_table = {
            '0': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'},
            '1': {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10'},
            '2': {'0': '2', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '10', '9': '11'},
            '3': {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '10', '8': '11', '9': '12'},
            '4': {'0': '4', '1': '5', '2': '6', '3': '7', '4': '8', '5': '9', '6': '10', '7': '11', '8': '12', '9': '13'},
            '5': {'0': '5', '1': '6', '2': '7', '3': '8', '4': '9', '5': '10', '6': '11', '7': '12', '8': '13', '9': '14'},
            '6': {'0': '6', '1': '7', '2': '8', '3': '9', '4': '10', '5': '11', '6': '12', '7': '13', '8': '14', '9': '15'},
            '7': {'0': '7', '1': '8', '2': '9', '3': '10', '4': '11', '5': '12', '6': '13', '7': '14', '8': '15', '9': '16'},
            '8': {'0': '8', '1': '9', '2': '10', '3': '11', '4': '12', '5': '13', '6': '14', '7': '15', '8': '16', '9': '17'},
            '9': {'0': '9', '1': '10', '2': '11', '3': '12', '4': '13', '5': '14', '6': '15', '7': '16', '8': '17', '9': '18'}
        }
        # 个位数乘法表
        self.multiplication_table = {
            '0': {'0': '0', '1': '0', '2': '0', '3': '0', '4': '0', '5': '0', '6': '0', '7': '0', '8': '0', '9': '0'},
            '1': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'},
            '2': {'0': '0', '1': '2', '2': '4', '3': '6', '4': '8', '5': '10', '6': '12', '7': '14', '8': '16', '9': '18'},
            '3': {'0': '0', '1': '3', '2': '6', '3': '9', '4': '12', '5': '15', '6': '18', '7': '21', '8': '24', '9': '27'},
            '4': {'0': '0', '1': '4', '2': '8', '3': '12', '4': '16', '5': '20', '6': '24', '7': '28', '8': '32', '9': '36'},
            '5': {'0': '0', '1': '5', '2': '10', '3': '15', '4': '20', '5': '25', '6': '30', '7': '35', '8': '40', '9': '45'},
            '6': {'0': '0', '1': '6', '2': '12', '3': '18', '4': '24', '5': '30', '6': '36', '7': '42', '8': '48', '9': '54'},
            '7': {'0': '0', '1': '7', '2': '14', '3': '21', '4': '28', '5': '35', '6': '42', '7': '49', '8': '56', '9': '63'},
            '8': {'0': '0', '1': '8', '2': '16', '3': '24', '4': '32', '5': '40', '6': '48', '7': '56', '8': '64', '9': '72'},
            '9': {'0': '0', '1': '9', '2': '18', '3': '27', '4': '36', '5': '45', '6': '54', '7': '63', '8': '72', '9': '81'}
        }

    def multiplication(self, number_x: str, number_y: str) -> str:
        """
        两个数字相乘（假设只会个位数相乘）
        :param number_x: 非负整数
        :param number_y: 非负整数
        :return: 乘积
        """
        result = '0'
        for index, x in enumerate(number_x[::-1]):
            sub_result = ''
            ten = '0'  # 十位数
            for y in number_y[::-1]:
                multiplication_result = self.multiplication_table[x][y]  # 个位数乘法
                addition_result = self.addition(multiplication_result, ten)  # 两个数字相加

                sub_result = addition_result[-1] + sub_result
                ten = addition_result[0] if len(addition_result) == 2 else '0'

            sub_result = sub_result if ten == '0' else ten + sub_result
            result = self.addition(result, sub_result + '0' * index)
        return result

    def addition(self, number_x: str, number_y: str) -> str:
        """
        两个数字相加（假设只会个位数加法）
        :param number_x: 非负整数
        :param number_y: 非负整数
        :return: 和
        """
        max_len = max(len(number_x), len(number_y))
        number_x = '0' * (max_len - len(number_x)) + number_x
        number_y = '0' * (max_len - len(number_y)) + number_y

        result = ''
        flag = False  # 是否进一位
        for x, y in zip(number_x[::-1], number_y[::-1]):  # 倒序
            addition_result = self.addition_table[x][y]  # 个位数加法

            if not flag:
                result = addition_result[-1] + result
                flag = True if len(addition_result) == 2 else False
            else:
                flag = True if len(addition_result) == 2 else False
                addition_result = self.addition_table[addition_result[-1]]['1']  # 个位数加法
                result = addition_result[-1] + result
                flag = True if len(addition_result) == 2 or flag else False

        result = '1' + result if flag else result
        return result


class RecIntMult(GradeSchool):
    """
    RecIntMult算法
    """
    def main(self, number_x: str, number_y: str) -> str:
        """
        两个数字相乘
        :param number_x: 非负整数
        :param number_y: 非负整数
        :return: 乘积
        """
        len_x, len_y = len(number_x), len(number_y)
        target_len = 2 ** math.ceil(math.log2(max(len_x, len_y)))  # 先决条件：位数是2的整数次方
        number_x = '0' * (target_len - len_x) + number_x
        number_y = '0' * (target_len - len_y) + number_y

        if target_len == 1:
            return self.multiplication_table[number_x][number_y]
        else:
            a, b = number_x[: target_len // 2], number_x[target_len // 2:]
            c, d = number_y[: target_len // 2], number_y[target_len // 2:]
            ac = self.main(a, c)
            ad = self.main(a, d)
            bc = self.main(b, c)
            bd = self.main(b, d)
            return self.addition(
                self.addition(
                    ac + '0' * target_len,
                    self.addition(ad, bc) + '0' * (target_len // 2)),
                bd
            )


class Karatsuba(GradeSchool):
    """
    Karatsuba算法
    """
    def main(self, number_x: str, number_y: str) -> str:
        """
        两个数字相乘
        :param number_x: 非负整数
        :param number_y: 非负整数
        :return: 乘积
        """
        len_x, len_y = len(number_x), len(number_y)
        target_len = 2 ** math.ceil(math.log2(max(len_x, len_y)))  # 先决条件：位数是2的整数次方
        number_x = '0' * (target_len - len_x) + number_x
        number_y = '0' * (target_len - len_y) + number_y

        if target_len == 1:
            return self.multiplication_table[number_x][number_y]
        else:
            a, b = number_x[: target_len // 2], number_x[target_len // 2:]
            c, d = number_y[: target_len // 2], number_y[target_len // 2:]

            p = self.addition(a, b)
            q = self.addition(c, d)

            ac = self.main(a, c)
            bd = self.main(b, d)
            pq = self.main(p, q)

            abcd = str(int(pq) - int(ac) - int(bd))

            return self.addition(
                self.addition(
                    ac + '0' * target_len,
                    abcd + '0' * (target_len // 2)),
                bd
            )


if __name__ == '__main__':
    t = GradeSchool()

    # # 小学算法-乘法-功能测试
    # a = '5678'
    # b = '1234'
    # e = t.multiplication(b, a)
    # print(e, int(a) * int(b))

    # # 小学算法-加法-功能测试
    # i = 0
    # while i < 10000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 10000000000000)
    #     random_integer2 = random.randint(0, 10000000000000)
    #     flag = t.addition(str(random_integer1), str(random_integer2)) == str(random_integer1 + random_integer2)
    #
    #     if not flag:
    #         print(
    #             random_integer1,
    #             random_integer2,
    #             t.addition(str(random_integer1), str(random_integer2)),
    #             random_integer1 + random_integer2
    #         )
    #     i += 1

    # # 小学算法-加法-性能测试
    # i = 0
    # start_time = time.time()
    # while i < 1000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 1000000000000000)
    #     random_integer2 = random.randint(0, 1000000000000000)
    #     # result = t.addition(str(random_integer1), str(random_integer2))  # 性能：8毫秒
    #     result = random_integer1 + random_integer2  # 性能：1毫秒，性能更优
    #     i += 1
    # end_time = time.time()
    # cost_time = (end_time - start_time) * 1000
    # print(round(cost_time, 2), 'ms')

    # # 小学算法-乘法-功能测试
    # i = 0
    # while i < 10000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 1000000000000000)
    #     random_integer2 = random.randint(0, 1000000000000000)
    #     flag = t.multiplication(str(random_integer1), str(random_integer2)) == str(random_integer1 * random_integer2)
    #
    #     if not flag:
    #         print(
    #             random_integer1,
    #             random_integer2,
    #             t.multiplication(str(random_integer1), str(random_integer2)),
    #             random_integer1 * random_integer2
    #         )
    #     i += 1

    # # 小学算法-乘法-性能测试
    # i = 0
    # start_time = time.time()
    # while i < 1000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 1000000000000000)
    #     random_integer2 = random.randint(0, 1000000000000000)
    #     # result = t.multiplication(str(random_integer1), str(random_integer2))  # 性能：377毫秒
    #     result = random_integer1 * random_integer2  # 性能：1毫秒，性能更优
    #     i += 1
    # end_time = time.time()
    # cost_time = (end_time - start_time) * 1000
    # print(round(cost_time, 2), 'ms')

    r = RecIntMult()

    # # RecIntMult算法-乘法-功能测试
    # i = 0
    # while i < 10000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 1000000000000000)
    #     random_integer2 = random.randint(0, 1000000000000000)
    #     flag = int(r.main(str(random_integer1), str(random_integer2))) == random_integer1 * random_integer2
    #
    #     if not flag:
    #         print(
    #             random_integer1,
    #             random_integer2,
    #             int(r.main(str(random_integer1), str(random_integer2))),
    #             random_integer1 * random_integer2
    #         )
    #     i += 1
    #
    # # RecIntMult算法-乘法-性能测试
    # i = 0
    # start_time = time.time()
    # while i < 1000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 1000000000000000)
    #     random_integer2 = random.randint(0, 1000000000000000)
    #     # result = t.multiplication(str(random_integer1), str(random_integer2))  # 性能：377毫秒
    #     # result = random_integer1 * random_integer2  # 性能：1毫秒，性能更优
    #     result = int(r.main(str(random_integer1), str(random_integer2)))  # 性能：353毫秒
    #     i += 1
    # end_time = time.time()
    # cost_time = (end_time - start_time) * 1000
    # print(round(cost_time, 2), 'ms')

    k = Karatsuba()

    # # Karatsuba算法-乘法-功能测试
    # i = 0
    # while i < 10000:
    #     # 生成一个0到10000000000000以内的非负整数
    #     random_integer1 = random.randint(0, 1000000000000000)
    #     random_integer2 = random.randint(0, 1000000000000000)
    #     flag = int(k.main(str(random_integer1), str(random_integer2))) == random_integer1 * random_integer2
    #
    #     if not flag:
    #         print(
    #             random_integer1,
    #             random_integer2,
    #             int(k.main(str(random_integer1), str(random_integer2))),
    #             random_integer1 * random_integer2
    #         )
    #     i += 1

    # Karatsuba算法-乘法-性能测试
    i = 0
    start_time = time.time()
    while i < 1000:
        # 生成一个0到10000000000000以内的非负整数
        random_integer1 = random.randint(0, 1000000000000000)
        random_integer2 = random.randint(0, 1000000000000000)
        # result = t.multiplication(str(random_integer1), str(random_integer2))  # 性能：377毫秒
        # result = random_integer1 * random_integer2  # 性能：1毫秒，性能更优
        # result = int(r.main(str(random_integer1), str(random_integer2)))  # 性能：353毫秒
        result = int(k.main(str(random_integer1), str(random_integer2)))  # 性能：478毫秒
        i += 1
    end_time = time.time()
    cost_time = (end_time - start_time) * 1000
    print(round(cost_time, 2), 'ms')


