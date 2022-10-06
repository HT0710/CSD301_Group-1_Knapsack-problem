
#Initializing the Items class with data variables - weight and value
from typing import List

class GreedyProgram:
    @staticmethod
    def findSolution(C : int, W : List[int], P : List[int]) -> List[int]:
        n = len(W)
        indexes = [x for x in range(n)]
        indexes.sort(key = lambda i : P[i]/W[i], reverse=True)

        usedCapacity = 0
        totalValue = 0
        result = []
        for i in range(0, n):
            if usedCapacity + W[indexes[i]] <= C:
                usedCapacity += W[indexes[i]]
                totalValue += P[indexes[i]]
                result.append(indexes[i])

        return result

