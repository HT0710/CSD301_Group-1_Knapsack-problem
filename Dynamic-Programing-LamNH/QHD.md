knapsack problem: là bài toán thuộc lĩnh vực tối ưu hóa tổ hợp 
đề cập đến một vấn đề
chung đó là cần chọn những món đồ nào để xếp vào
trong một cái ba lô có giới hạn về khối lượng để
mang đi sao cho một tiêu chí nào đó được tối ưu
(như giá trị, nhu cầu sử dụng, …).


n : số đồ vật 
b : trọng lượng túi

=>  i(1...n) : đồ vật i từ 1 tới n 
    L(0...b) : trọng lượng tối đa của túi

    Ta nhận thấy rằng: Giá trị của cái túi phụ thuộc vào 2 yếu tố: Có bao nhiêu vật đang được xét và trọng lượng còn lại cái túi có thể chứa được, do vậy chúng ta có 2 đại lượng biến thiên. Cho nên hàm mục tiêu sẽ phụ thuộc vào hai đại lượng biến thiên. Do vậy bảng phương án của chúng ta sẽ là bảng 2 chiều.

    Gọi F[i,L] là tổng giá trị lớn nhất của cái túi khi xét từ vật 1 đến vật i và trọng lượng của cái túi chưa vượt quá L. Với giới hạn L, việc chọn tối ưu trong số các vật {1,2,…,i-1,i} để có giá trị lớn nhất sẽ có hai khả năng:

    Nếu không chọn vật thứ i thì F[i,L] là giá trị lớn nhất có thể chọn trong số các vật {1,2,…,i-1} với giới hạn trọng lượng là L, tức là:

    F[i,L]:=F[i-1,L].

    Nếu có chọn vật thứ i (phải thỏa điều kiện W[i] ≤ L) thì F[i,L] bằng giá trị vật thứ i là V[i] cộng với giá trị lớn nhất có thể có được bằng cách chọn trong số các vật {1,2,…,i-1} với giới hạn trọng lượng L-W[i] tức là về mặt giá trị thu được:

    F[i,L]:=V[i]+F[i-1,L-W[i]]

    Vậy chúng ta phải xem xét xem nếu chọn vật i hay không chọn vật i thì sẽ tốt hơn. Công thức: 

    F[0,L] = 0 
    F[i,L] = 0
    F[i,L]= max(F[i-1,L], V[i]+F[i-1,L-W[i]]