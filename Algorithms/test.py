from numpy import append

C = 50
W = [20, 30, 10]
P = [100, 120 , 60]
n = len(W)

WP = [P[i]/W[i] for i in range(len(W))]
indexes = [x for x in range(n)]
for i in range(0, n - 1):
    for j in range (n - i - 1):
        if  WP[j] < WP[j + 1]:
            WP[j], WP[j + 1] = WP[j + 1], WP[j]
            indexes[j], indexes[j + 1] = indexes[j + 1], indexes[j]

def Function(C, W, P):
    usedCapacity = 0
    totalValue = 0
    result = []
    for i in range(0, len(W)):
        if usedCapacity + W[indexes[i]] <= C:
            usedCapacity += W[indexes[i]]
            totalValue += P[indexes[i]]
            result.append(indexes[i])
        else:
            break
    return result
print(Function(C, W, P))