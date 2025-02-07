mạnh với một bảng đã sắp xếp. Vì ko duyệt hết mảng và so sánh nếu phù hợp thì so sánh tiếp.

arr = [7,6,5,1,2,4]

luôn lấy số index 1 làm chuẩn
lưu số xét vào một biến
set = 6
1. lấy 6 so sánh với 7 nếu 7 > 6 thì thay 6 = 7
dừng loop
6,7,5,1,2,4
index = 2 => set = 5
2. Lấy index so với 7 nếu 7>index swap vị trí index = 7
6,7,7,1,2,4
Lấy index so với 6 nếu 6>index swap vị trí index = 6
6,6,7,1,2,4
thay số cuối loop bằng index
5,6,7,1,2,4