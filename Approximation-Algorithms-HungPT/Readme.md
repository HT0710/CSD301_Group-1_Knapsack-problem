<h1 align="center">Approximation Algorithms</h1>

## Define
- Thuật toán xấp xỉ là các thuật toán tìm lời giải xấp xỉ cho các bài toán tối ưu hóa.
- Kỹ thuật này không đảm bảo giải pháp tốt nhất. Mục tiêu của thuật toán xấp xỉ là đến gần nhất có thể với giải pháp tối ưu trong thời gian đa thức.
- Thường được sử dụng cho các bài toán NP-khó, hoặc các bài toán có thuật toán đa thức nhưng quá chậm cho dữ liệu lớn.

#### *[# Bài toán NP-khó](https://vi.wikipedia.org/wiki/NP-kh%C3%B3)*
NP-khó là một tập hợp các bài toán trong lý thuyết độ phức tạp tính toán "ít nhất là khó ngang bất kì bài toán nào trong NP".

(NP: độ phức tạp)

## About Algorithm 
Từ góc độ tính xấp xỉ, các bài toán NP-khó có độ khó rất khác nhau.

Có những bài toán như **[knapsack](https://vi.wikipedia.org/wiki/B%C3%A0i_to%C3%A1n_x%E1%BA%BFp_ba_l%C3%B4)** có thuật toán xấp xỉ với bất kì tỉ lệ nào lớn hơn 1.

Có những bài toán khác như **[clique](https://vi.wikipedia.org/wiki/Clique)** không thể tính xấp xỉ với tỉ lệ $a^{1-ε}$ với mọi ε > 0 trừ phi một giả thuyết phổ biến trong lý thuyết độ phức tạp tính toán là sai.

## Features
- Đảm bảo chạy trong thời gian đa thức mặc dù nó không đảm bảo giải pháp hiệu quả nhất.
- Đảm bảo tìm ra giải pháp có độ chính xác cao và chất lượng hàng đầu (giả sử trong vòng 1% của mức tối ưu).
- Được sử dụng để nhận được câu trả lời gần với giải pháp (tối ưu) của một bài toán tối ưu hóa trong thời gian đa thức.

### Case 1:
Giả sử rằng chúng ta đang làm một bài toán tối ưu hóa, trong đó mỗi giải pháp tiềm năng đều có một chi phí (cost) và chúng ta muốn tìm một giải pháp gần như tối ưu.

Tùy thuộc vào vấn đề, chúng tôi có thể xác định một giải pháp tối ưu là một giải pháp với chi phí tối đa có thể có hoặc một giải pháp với chi phí tối thiểu có thể có, tức là vấn đề có thể là một bài toán tối đa hóa hoặc tối thiểu hóa.

Thuật toán cho một bài toán có tỷ lệ thích hợp là P(n) nếu với bất kì kích thước đầu vào n nào, chi phí C của giải pháp tạo ra bởi thuật toán nằm trong hệ số P(n) của chi phí C* của một giải pháp tối ưu như sau:
```
max(C/C*,C*/C) <= P(n)
```

### Case 2:
Nếu một thuật toán đạt đến tỷ lệ xấp xỉ P(n), thì chúng ta gọi nó là thuật toán xấp xỉ P(n):
- Đối với bài toán tối đa hóa (maximization), 0 < C < C* và tỷ lệ C* / C cho biết hệ số mà chi phí của một giải pháp tối ưu lớn hơn chi phí của thuật toán gần đúng.
- Đối với bài toán tối thiểu hóa (minimization), 0 < C* < C và tỷ lệ C / C* cho biết hệ số mà chi phí của một giải pháp gần đúng lớn hơn chi phí của một giải pháp tối ưu.

## Some examples of the Approximation algorithm
#### 1. [The Vertex Cover Problem](https://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm-2/)
Trong bài toán này, bài toán tối ưu là tìm vertex cover có ít đỉnh nhất.

#### 2. [Travelling Salesman Problem](https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/)
Trong bài toán này, bài toán tối ưu hóa là tìm chu trình ngắn nhất.

#### 3. [The Set Covering Problem](https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/)
Đây là một bài toán tối ưu hóa mô hình hóa nhiều bài toán yêu cầu tài nguyên được phân bổ. Ở đây, một tỷ lệ xấp xỉ logarit được sử dụng.

#### 4. [The Subset Sum Problem](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
Trong bài toán Tổng tập con, bài toán tối ưu hóa là tìm một tập con gồm ${x^1, x^2, x^3… x^n}$ có tổng càng lớn càng tốt nhưng không lớn hơn giá trị đích t.

## Algorithm design techniques
Hiện nay, đã có một số kỹ thuật được thiết lập để thiết kế các thuật toán xấp xỉ, bao gồm:
1. [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
2. [Local search](https://en.wikipedia.org/wiki/Local_search_(optimization))
3. Enumeration và [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming)
4. Giải quyết bài toán [convex programming](https://en.wikipedia.org/wiki/Convex_programming) để có một nghiệm phân số. Sau đó, chuyển phân số này thành một giải pháp khả thi bằng một số làm tròn thích hợp. Các cách phổ biến bao gồm:
- [Linear programming](https://en.wikipedia.org/wiki/Linear_programming)
- [Semidefinite programming](https://en.wikipedia.org/wiki/Semidefinite_programming)
5. Primal-dual methods
6. Dual fitting
7. Metric embedding
8. Random sampling và kết hợp với các phương pháp trên
