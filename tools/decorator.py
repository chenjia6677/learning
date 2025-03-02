import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} 执行时间：{(end - start) * 1000:.2f} 毫秒')
        return result
    return wrapper


