from typing import List


class BruteForce:

    @staticmethod
    def findSolution(C : int, W : List[int], P : List[int]) -> List[int]:
        '''
        Find a solution of knapsack problem using Brute Force algorithms

        @Parameters:
        ----------
            - C : weight of knapsack
            - W : list weight of items
            - P : list price of items

        @Return
        ----------
        List indexes of selected items
        '''

        # Number of items
        n = len(W)
        result = BruteForce.__knapSack(C, W, P, n)

        return result[1]

    @staticmethod
    def __knapSack(mW: int, w, v, n):

        if (mW == 0 or n == 0):
            return [0, []]

        if (w[n-1] > mW):
            return BruteForce.__knapSack(mW, w, v, n-1)

        set1 = BruteForce.__knapSack(mW-w[n-1], w, v, n-1)
        set2 = BruteForce.__knapSack(mW, w, v, n-1)

        if (set1[0]+v[n-1] > set2[0]):
            set1[1].append(n-1)
            set1[0] += v[n-1]
            return set1
        else:
            return set2