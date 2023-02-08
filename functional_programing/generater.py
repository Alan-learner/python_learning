# 表达式生成器
generater = (x for x in range(20) if x % 2 == 0)


# 函数式生成器
def gen_func(times):
    x, y = 0, 1
    n = 0
    while n <= times:
        yield y
        x, y = y, (x + y)
        n += 1


def main():
    x1 = generater.__next__()
    x2 = next(generater)
    print(x1, x2)
    for k in generater:
        print(k)


def main2():
    # 4种访问生成器的方法
    g = gen_func(times=15)
    print(next(g))
    print(g.__next__())
    # for k in g:
    #     print(k)
    g.send(None)
    print(g.send("xyz"))
    print(g.send("123"))
    print(g.send("xyz"))
    print(g.send("123"))
    print(g.send("xyz"))
    print(g.send("123"))


if __name__ == '__main__':
    # main()
    main2()
