
from typing import List

class DynamicPrograming:
    @staticmethod
    def findSolution(C : int, W : List[int], P : List[int]) -> List[int]:
        n = len(W)

        if sum(W) <= C:
            return [x for x in range(n)]
        
        dp = [0] * (C+1)  # Making the dp array
        di = [-1] * (C+1)

        for i in range(1, n+1):  # taking first i elements
            for w in range(C, 0, -1):  # starting from back,so that we also have data of
                                    # previous computation when taking i-1 items
                if W[i-1] <= w:
                    # finding the maximum value
                    # dp[w] = max(dp[w], dp[w-W[i-1]]+P[i-1])
                    if dp[w] < dp[w - W[i-1]]+P[i-1]:
                        di[w] = i - 1
                        dp[w] = dp[w - W[i-1]]+P[i-1]
        result = []
        selected = []
        print(di)
        i = C
        while i > 0 and not di[i] in selected:
            result = [di[i]] + result
            selected.append(di[i])
            i -= W[di[i]] 

        return result  # returning the maximum value of knapsack
