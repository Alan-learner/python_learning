# encoding: utf-8
# author: Alan-learner
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        idx = (1 << (n - 1)) + k - 1

        def get_val(index):
            if index == 1:
                return 0
            if get_val(index // 2) == 0:
                if index % 2 == 0:
                    return 0
                else:
                    return 1
            else:
                if index % 2 == 0:
                    return 1
                else:
                    return 0

        return get_val(idx)


def main():
    s = Solution()
    res = s.kthGrammar(n=2, k=2)
    print(res)


if __name__ == '__main__':
    main()
