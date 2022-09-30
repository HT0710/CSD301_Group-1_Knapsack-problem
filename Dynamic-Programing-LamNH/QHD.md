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
    khi đó mVal(n,b) là giá trị lớn nhất mang được với n đồ vật và b trọng lượng

    giả sử ta đã nhét đc đồ vật i - 1 vào túi 
    gọi mVal(i - 1, L) : là giá trị lớn nhất mang đi đc với (i - 1) đồ vật 
                        với trọng lượng L 
    => giá trị túi lúc mang (i - 1) đồ vật và L là mVal[(i -1), L]
    khi đó ta xét đồ vật thứ i với L: 
    cho mVal(i, L) = mVal[(i -1), L]
    nếu L >= w[i] (tức có thể mang theo i) 
    và mVal[(i - 1), L - w[i]] + v[i](giá trị của đồ vật i) > mVal(i, L)
    => cập nhật lại giá trị  mVal(i, L) = mVal[(i - 1), L - w[i]] + v[i]
    