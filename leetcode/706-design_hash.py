# encoding: utf-8
# author: Alan-learner


class MyHashMap:

    def __init__(self):
        self.data = [-1] * (10 ** 6 + 3)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1


def main():
    pass


if __name__ == '__main__':
    main()
