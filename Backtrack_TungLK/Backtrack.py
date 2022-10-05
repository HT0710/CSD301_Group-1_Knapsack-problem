import sys

sys.setrecursionlimit(10**8)

c = 0


def main():
    P = [160, 100, 120]
    W = [10, 20, 30]

    alg = Backtrack(W, P)

    print(alg.findSolution(50))

    print("Total Recursive Steps: ", c)


class Backtrack:
    def __init__(self, W, P):
        self.__W = W
        self.__P = P

    def get_weight(self):
        return self.__W

    def get_value(self):
        return self.__P

    def findSolution(self, C):
        n = len(self.__P)
        result = self.__knapSack(C, self.__W, self.__P, n)

        return result

    def __knapSack(self, mW, w, v, n):
        # counter how many time recursive function is called.
        global c
        c += 1

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


if __name__ == '__main__':
    main()
