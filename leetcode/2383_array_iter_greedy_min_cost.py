# encoding: utf-8
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list, experience: list) -> int:
        train = 0
        eng_cost = sum(energy) - initialEnergy
        if eng_cost >= 0:
            train = eng_cost + 1
        for exp in experience:
            if exp >= initialExperience:
                left = exp - initialExperience + 1
                train += left
                initialExperience += left
            initialExperience += exp
        return train


def main():
    pass


if __name__ == '__main__':
    main()
