from functools import reduce

data_list = [7, 4, 5, 6, 2]


def get_variable_name(variable):
    dic = dict()
    loc = locals()
    for k, v in loc.items():
        if loc[k] == variable:
            return k


# map,reduce,filter

maped_list = list(map(lambda x: x ** 2, data_list))

reduce_num = reduce(lambda x, y: x % y, data_list)

loc = locals()
i = id(reduce_num)

filter_list = list(filter(lambda x: x % 2 == 1, data_list))


def get_func(leneh):
    if not leneh:
        return lambda x: x ** 2
    elif leneh == 1:
        return lambda x: x ** 3
    else:
        return lambda x: x * 2


def main():
    cnt = 0
    for val in [data_list, maped_list, reduce_num, filter_list]:
        func = get_func(cnt)
        print(f"val{cnt}:{val}  func:{func(cnt)}")
        cnt += 1


if __name__ == '__main__':
    main()
