# Brute Force
Vẽ giúp tui trong ppt cái biểu đồ cây dạng :

![BF](/Nghiatnh-BruteForce-MITM/Complexity/bruteforce_complexity.png "BF")

-> N item thì độ phức tạp thời gian là O(2^n) cho toàn bộ case.

-> Độ phức tạp bộ nhớ là O(n)

    Time Complexity: O(2n). 
    As there are redundant subproblems.
    Auxiliary Space :O(1) + O(N). 
    As no extra data structure has been used for storing values but O(N) auxiliary stack space(ASS) has been used for recursion stack.
    --- Geeksforgeeks --- 


# Meet-int-the-middle
Trong trường hợp đặc biệt W[i] = P[i] thì ta có một phương pháp giúp giảm thời gian thực thi đó là Meet-in-the-middle

Vẽ giúp tui cái hình minh họa để tính độ phức tạp

![MITM](/Nghiatnh-BruteForce-MITM/Complexity/mitm_complexity.png "MITM")

    Độ phức tạp về bộ nhớ O(2^n/2)
    Độ phức tạp thời gian O(2^n/2).log(2^n/2)