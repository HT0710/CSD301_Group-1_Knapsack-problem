from typing import List


class Genetic:

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

        return []