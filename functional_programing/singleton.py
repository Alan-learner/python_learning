import time


class Singleton:
    _instance = None
    __flag = False

    def __new__(cls, *args, **kwargs):
        print("__new__执行了")
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # cls._instance = object.__new__(cls) # 与上面写法等价
        return cls._instance

    def __init__(self):
        if not self.__flag:
            print("__init__执行了")
            self.__flag = True


if __name__ == '__main__':
    s = Singleton()
    s2 = Singleton()
    print(s)
    print(s2)
