import queue

class Node:
    def __init__(self, level, profit, weight):
        self.level = level # The level within the tree (depth)
        self.profit = profit # The total profit
        self.weight = weight # The total weight
   # list of items our node contains

# This is essentially the brute force solution to the fractional knapsack
def getBound(u, numItems, knapsackSize, weight, profit):
    if u.weight >= knapsackSize: return 0
    else:
        upperBound = u.profit
        totalWeight = u.weight
        j = u.level + 1
        while j < numItems and totalWeight + weight[j] <= knapsackSize:
            upperBound += profit[j]
            totalWeight += weight[j]
            j += 1
        if j < numItems:
            upperBound += ((knapsackSize - totalWeight) * (profit[j]/weight[j]))
        return upperBound 


def solveKnapsack(weights, profits, knapsackSize):
    numItems = len(weights)
    q = queue.Queue()
    root = Node(-1, 0, 0)    
    q.put(root)

    maxProfit = 0
    bound = 0
    while not q.empty():
        a = []
        v = q.get() # Get the next item on the queue
        #print(v.weight)
        uLevel = v.level + 1 
        u = Node(uLevel, v.profit + profits[uLevel], v.weight + weights[uLevel])

        bound = getBound(u, numItems, knapsackSize, weights, profits)

        if u.weight <= knapsackSize and u.profit > maxProfit:
            maxProfit = u.profit
            
        if bound > maxProfit:    
            q.put(u)

        u = Node(uLevel, v.profit, v.weight)
        bound = getBound(u, numItems, knapsackSize, weights, profits)

        if bound > maxProfit:
            q.put(u)
    return maxProfit
    

if __name__ == "__main__":
    C = 15
    v = [10, 10, 12, 18]
    w = [2,4,6,9]
    print(solveKnapsack(w, v, C))