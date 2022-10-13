from inspect import stack
from typing import List


class Node:
    def __init__(self, weight, index) -> None:
        self.weight = weight
        self.index = index
        self.next = 0

class BruteForceMemorization:

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

        K = [[-1 for x in range(n + 1)] for x in range(C + 1)]
        
        root = Node(C, 0)
        stk = stack()
        stk.clear()
        stk.append(root)
        maxNode : Node = root
        maxProfit = -1

        count = 0

        while len(stk) > 0:
            count += 1
            s : Node = stk.pop()
            if s.index == n or s.weight == 0:
                K[s.weight][s.index] = 0
                continue

            if W[s.index] > s.weight:
                if K[s.weight][s.index + 1] == -1:
                    stk.append(s)
                    stk.append(Node(s.weight, s.index + 1))
                else:
                    K[s.weight][s.index] = K[s.weight][s.index + 1]
                continue

            if K[s.weight][s.index + 1] == -1 or K[s.weight - W[s.index]][s.index + 1] == -1:
                stk.append(s)
                if K[s.weight][s.index + 1] == -1:
                    stk.append(Node(s.weight, s.index + 1))
                if K[s.weight - W[s.index]][s.index + 1] == -1:
                    stk.append(Node(s.weight - W[s.index], s.index + 1))
            else:
                K[s.weight][s.index] = max(K[s.weight][s.index + 1], K[s.weight - W[s.index]][s.index + 1] + P[s.index])
                if K[s.weight][s.index] > K[maxNode.weight][maxNode.index]:
                    maxNode = s
        
        curNode = maxNode
        result = []
        
        while curNode:
            result.append(curNode.index)
        return result

# print(BruteForceMemorization.findSolution(55, [5,20,30,10],[500,100,120,60]))