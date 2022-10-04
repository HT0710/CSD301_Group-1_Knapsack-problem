# Hướng dẫn phân chia code
Để thuận tiện trong việc merge code và phát triển GUI, các bạn chia class và file theo cấu trúc tương tự như sau:

- Tạo một file <tên thuật toán>.py bên trong folder Algorithms
    + Ví dụ: Mình muốn đóng góp thêm cách giải bài toán Knapsack bằng thuật toán Dynamic Programing cơ bản thì mình sẽ tạo một file mới có tên là Dynamic-Programing-Basic.py bên trong folder Algorithms
- Tạo một class có tên cùng tên với file vừa tạo
- Trong class phải có một hàm static public tên là findSolution(C, W, P). Với:
  - C : int là khối lượng tối đa của túi.
  - W : List[int] là danh sách khối lượng các item.
  - P : List[int] là danh sách giá trị các item tương ứng với W
- Kết quả trả về của hàm findSolution là một danh sách các chỉ số của item được bỏ vào túi. Ví dụ, hàm trả về [0, 5] thì W[0], W[5] lần lượt là khối lượng của các item được bỏ vào túi và P[0], P[5] là các giá trị tương ứng của item.
- Bên trong class các bạn tùy ý tạo các function để hỗ trợ việc giải bài toán.
- Nên thể đánh dấu lại kiểu dữ liệu của biến để người khác dễ đọc (nếu không thích thì thôi, nhưng khuyến khích nên để kiểu dữ liệu cho dễ đọc).
- <b>QUAN TRỌNG:</b> Phải comment code, tối thiểu là ở mức độ function (tức là comment function đó có tác dụng gì, các biến đầu vào và đầu ra có ý nghĩa gì). 

Các bạn xem code mẫu [ở đây](./Algorithms/CodingGuideExample.py)

Mục đích của việc này là:
- Ta chia code frontend và backend độc lập với nhau.
- Tránh gây xung đột vì code ở các file khác nhau.
- Dễ kiểm soát lỗi hơn.
- Nhiều người cùng code sẽ nhanh hơn 1 người.