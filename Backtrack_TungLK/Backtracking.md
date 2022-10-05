									Knapsack Problem -- Backtracking
Given n positive weights wi, n positive profits pi , and a positive number M which is the knapsack capacity, the 0/1 knapsack problem calls for choosing a subset of the weights such that

S i = 1 to k wixi £ M and
S i = 1 to k pixi is maximizd

The x's constitute a zero-one valued vector.
The solution space for this problen consists of the 2n distinct ways to assign zero or one values to the x's.
Thus the solution space is the same as that for the sum of the subsets problem.

Bounding function is needed to help kill some live nodes without actually expanding them.
A good bounding function for this problem is obtained by using an upper bound on the value of the best feasible solution obtainable by expanding the given live node and any of its descendants. If this upper bound is not higher than the value of the best solution determined so far then that live node may be killed.

Here we use the fixed tuple size formulation.
If at node Z the values of xi , 1 £ i £ k have already been determined, then an upper bound for Z can be obtained by relaxing the requirement xi = 0 or 1 to 0 £ xi £ 1 for k+1 £ i £ n and use the greedy method to solve the relaxed problem.

Procedure Bound(p,w,k,M) determines an upper bound on the best solution obtainable by expanding any node Z at level k+1 of the state space tree.

The object weights and profits are W(i) and P(i).
p = S i = 1 to k P(i)X(i) and it is assumed that P(i)/W(i) ³ P(i+1)/W(i+1), 1 £ i £ n

procedure BOUND(p,w,k,M)
// p: the current profit total
// w: the current weight total
// k : the index of the last removed item
// M : the knapsack size
// the return result is a new profit

global  n , P(1:n) , W(1:n)
integer k, i l real b,c,p,w, M
      b := p ;  c := w
      for  i := k+1 to n do 
           c := c + W(i)
           if c < M then b := b + P(j)
                    else  return (b + (1 - (c - M)/W(i))*P(i))
           endif
      repeat
      return (b)
end BOUND

Remark :

It follows that the bound for a feasible left child ( x(k) = 1) of a node Z is the same as that for Z. Hence , the bounding function need not be used whenever the backtracking algorithm makes a move to the left child of the node. Since the backtracking algorithm will attempt make a left child move whenever given a choice between a left and right child, the bounding function need be used only after a series of successful left child moves ,(i,e, moves to feasible left child).


procedure Knapsack(M,n,W,P, fw,fp,X)
// M : the size of the knapsack
// n : the number of the weights and profits
// W(1:n) : the weights
// P(1:n) : the corresponding profits ;  P(i)/W(i) ³  P(i+1)/W(i+1), 
// fw : the final weight of the knapsack
// fp : the final maximum profit
// X(1:n), either zero or one ; X(k) = 0  if W(k) is not in the knapsack else X(k) = 1


1.  integer n,k, Y(1:n), i , X(1:n) ; real M, W(1:n), P(1:n), fw, fp, cw, cp ;
2.    cw := cp := 0  ; k := 1 ; fp := -1    // cw = current weight, cp = current profit
3.  loop
4.  while  k £ n  and cw + W(k) £ M do // place k into knapsack
5.      cw := cw + W(k) ; cp := cp + P(k) ; Y(k) := 1 ; k := k+1
6.  repeat
7.  if k > n then fp := cp; fw := cw ; k := n ; X := Y   // update the solution
8.  else  Y(k) := 0     // M is exceeded so object k does not fit
9.  endif
10. while BOUND(cp,cw,k,M) £ fp do // after fp is set above, BOUND = fp
11.      while k <>  0 and Y(k) <>  1 do 
12.          k := k -1   // find the last weight included in the knapsack
13.      repeat
14.      if k = 0 then return   endif    // the algorithm ends here
15.      Y(k) := 0 ; cw := cw - W(k) ; cp := cp - P(k)  // remove the k-th item
16.  repeat
17.  k := k+1
18.  repeat
19.  end knapsack



Algorithm : Backtracking solution to the 0/1 knapsack problem

https://condor.depaul.edu/ichu/csc491/notes/wk8/knapsack.html?fbclid=IwAR0CI9RvA5tjzZoQGhOtKSc949udKODaVSqwFnH89o5HWYqfF30gk_FEh4Y