from typing import List
import itertools


def __main():
    P = [60, 100, 140, 200]
    W = [10, 20, 30, 40]
    C = 70
    print(BruteForce.findSolution(C, W, P))


class BruteForce:
    @staticmethod
    def findSolution(C: int, W: List[int], P: List[int]) -> List[int]:
        n = len(W)
        max_P = BruteForce.__algorithm(C, W, P, n)

        return BruteForce.__result(P, max_P)

    @staticmethod
    def __algorithm(C, W, P, n):
        if n == 0 or C == 0:
            return 0

        # If weight of the nth item is
        # more than Knapsack of capacity W,
        # then this item cannot be included
        # in the optimal solution
        if (W[n-1] > C):
            return BruteForce.__algorithm(C, W, P, n-1)

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        else:
            return max(
                P[n-1] + BruteForce.__algorithm(C-W[n-1], W, P, n-1),
                BruteForce.__algorithm(C, W, P, n-1))

    @staticmethod
    def __result(P: List[int], mP: int):
        # for i in range(len(P)):
        #     for j in itertools.combinations(P, i):
        #         if (sum(j) == mP):
        #             return [P.index(i) for i in j]
        return []


if __name__ == '__main__':
    __main()
