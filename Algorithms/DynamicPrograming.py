
from typing import List

class DynamicPrograming:
    @staticmethod
    def findSolution(C : int, W : List[int], P : List[int]) -> List[int]:
        n = len(W)
        K = [[0 for x in range(C + 1)] for x in range(n + 1)]
 
        # Build table K[][] in bottom up manner
        for i in range(n + 1):
            for w in range(C + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif W[i-1] <= w:
                    K[i][w] = max(P[i-1]
                            + K[i-1][w-W[i-1]], 
                                K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]

        i = n
        w = C
        result = []
        while i > 0:
            if K[i][w] != K[i - 1][w]:
                result.append(i - 1)
                w -= W[i - 1]
                i -= 1
            else:
                i -= 1
        return result