import queue
from time import time
from typing import List

class BranchAndBound:
    @staticmethod
    def findSolution(C : int, W : List[int], P : List[int]) -> List[int]:
        n = len(W)
        indexes = [x for x in range(n)]
        indexes.sort(key = lambda i : P[i]/W[i], reverse=True)
        class Node:
            def __init__(self, level, profit, weight, index, parent):
                self.level = level # The level within the tree (depth)
                self.profit = profit # The total profit
                self.weight = weight # The total weight
                self.parent = parent # The previous node
                self.index = index # Index of weight and profit

            def __str__(self) -> str:
                return "Node: W = {}, P = {}, L = {}".format(self.weight, self.profit, self.level)
        # list of items our node contains

        # This is essentially the brute force solution to the fractional knapsack
        def getBound(u, numItems, knapsackSize, weight, profit):
            if u.weight >= knapsackSize: return 0
            else:
                upperBound = u.profit
                totalWeight = u.weight
                j = u.level + 1
                while j < numItems and totalWeight + weight[indexes[j]] <= knapsackSize:
                    upperBound += profit[indexes[j]]
                    totalWeight += weight[indexes[j]]
                    j += 1

                if j < numItems:
                    upperBound += ((knapsackSize - totalWeight) * (profit[indexes[j]]/weight[indexes[j]]))
                return upperBound 


        def solveKnapsack(knapsackSize, weights, profits):

            numItems = len(weights)
            q = queue.Queue()
            root = Node(-1, 0, 0, -1, None)    
            q.put(root)

            maxProfit = 0
            maxU = None
            bound = 0
            while not q.empty():
                v = q.get() # Get the next item on the queue\
                uLevel = v.level + 1
                u = Node(uLevel, v.profit + profits[indexes[uLevel]], v.weight + weights[indexes[uLevel]], uLevel, v)
                bound = getBound(u, numItems, knapsackSize, weights, profits)

                if u.weight <= knapsackSize and u.profit > maxProfit:
                    maxProfit = u.profit
                    maxU = u
                    
                if bound > maxProfit:    
                    q.put(u)

                u = Node(uLevel, v.profit, v.weight, v.level, v.parent)
                bound = getBound(u, numItems, knapsackSize, weights, profits)

                if bound > maxProfit:
                    q.put(u)
            curNode = maxU
            result = []
            while curNode and curNode.level != -1:
                result.append(indexes[curNode.index])
                curNode = curNode.parent
            return result

        return solveKnapsack(C, W, P)