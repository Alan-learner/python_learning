from collections.abc import Iterable, Iterator


def is_iterable(obj):
    if isinstance(obj, Iterable):
        print("yes")
        return True
    else:
        print("no")
        return False


def is_iterator(obj):
    if isinstance(obj, Iterator):
        print("yes")
        return True
    else:
        print("no")
        return False


def main():
    is_iterable("df")
    is_iterable([])
    is_iterable({})
    is_iterable(())
    is_iterable(set())
    is_iterator("df")
    is_iterator(iter([]))
    is_iterator({})
    is_iterator(iter((3, 5)))
    is_iterator(set())


if __name__ == '__main__':
    main()
