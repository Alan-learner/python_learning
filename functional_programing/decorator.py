import time
from functools import wraps


def decorator(func):
    @wraps(func)  # 使用func来包装inner函数，用于打包内置函数传递给（调用的）被装饰的高阶函数，使被装饰的函数名称不变
    def inner(*args, **kwargs):
        print("[info] -- %s" % time.strftime("%H:%M:%S", time.localtime()))
        print("函数的入参为:")
        for arg in args:
            print(arg, type(arg))
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        during = end_time - start_time
        print("函数运行时长为 {} s".format(during))
        print("函数返回值为：{} ,数据类型为：{}".format(ret, type(ret)))
        return ret

    return inner


@decorator  # 等价于 multiply = decorator(multiply)
def multiply(a, b):
    return a * b


# multiply = decorator(multiply) # 还原调用接口形式，与装饰器写法等价

if __name__ == '__main__':
    multiply(3, "5")
    print(multiply.__name__)
