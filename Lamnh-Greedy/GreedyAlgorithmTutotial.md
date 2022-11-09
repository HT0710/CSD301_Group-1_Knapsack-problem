1. Algorithm 
// Input: 
X: An array of n items
V: An array of profit associated with each item
W: An array of weight associated with each item
M: Capacity of knapsack

// Output : 	
SW: Weight of selected items
SP: Profit of selected items
// Items are presorted in decreasing order of pi = vi / wi ratio

S ← Φ	  // Set of selected items, initially empty
SW ← 0    // weight of selected items
SP ← 0    // profit of selected items
i ← 1

while i ≤ n do
    if (SW + w[i]) ≤ M then
        S ← S ∪ X[i]                
        SW ← SW + W[i]
        SP ← SP + V[i]
        i ← i + 1
end

2. Time Complexity
The main time taking step is the sorting of all items in decreasing order of their value / weight ratio.
Using merge sort or heap sort, n items can be sorted in O(nlog2n) time
The average time complexity of Quick Sort is O(nlogn).
To select the items, we need one scan to this sorted list, which will take O(n) time.
So the total time required is
T(n) = O(nlog2n) + O(n) = O(nlog2n).
Therefore, total time taken including the sort is O(nlogn).
                                    Auxiliary Space: O(N)