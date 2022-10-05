class Backtrack:
    def __init__(self, W: list, P: list):
        self.__W = W
        self.__P = P

    def findSolution(self, C: int):
        w = self.__W
        v = self.__P
        n = len(self.__P)
        result = self.__knapSack(C, w, v, n)

        return result[1]

    def __knapSack(self, mW: int, w, v, n):

        if (mW == 0 or n == 0):
            return [0, []]

        if (w[n-1] > mW):
            return self.__knapSack(mW, w, v, n-1)

        set1 = self.__knapSack(mW-w[n-1], w, v, n-1)
        set2 = self.__knapSack(mW, w, v, n-1)

        if (set1[0]+v[n-1] > set2[0]):
            set1[1].append(n-1)
            set1[0] += v[n-1]
            return set1
        else:
            return set2