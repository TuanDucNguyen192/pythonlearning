a = int(input("Nhap so nguyen a "))  
b = int(input("Nhap so nguyen b "))  
sum = 0  

if a % 2 != 0:  
    a += 1  # Nếu `a` là số lẻ, tăng lên 1 để thành số chẵn  

for a in range(a, b, 2):  # Lặp qua các số chẵn từ `a` đến `b-1`
    sum += a  # Cộng giá trị `a` vào tổng

print(sum)  # In kết quả tổng
🧐 Giải thích từng phần
🔹 1. Nhập dữ liệu
Người dùng nhập hai số nguyên a và b.
Ví dụ:

ini
Copy
Edit
a = 3
b = 10
🔹 2. Kiểm tra a có phải số chẵn không?
python
Copy
Edit
if a % 2 != 0:  
    a += 1  
Nếu a là số lẻ, tăng a lên 1 để thành số chẵn.
Nếu a đã là số chẵn, giữ nguyên.
📌 Ví dụ với a = 3

3 % 2 != 0 (vì 3 là số lẻ) → a = 3 + 1 = 4
📌 Ví dụ với a = 4

4 % 2 == 0 (số chẵn) → a giữ nguyên.
🔹 3. Vòng lặp for
python
Copy
Edit
for a in range(a, b, 2):
    sum += a
range(a, b, 2) tạo dãy số từ a đến trước b, với bước nhảy 2.
Mỗi lần lặp, giá trị a được cộng vào biến sum.
🔹 4. Phân tích từng lần lặp
📌 Ví dụ 1: a = 3, b = 10
Sau khi kiểm tra số chẵn, a trở thành 4.
Dãy số trong range(4, 10, 2) là: 4, 6, 8

Lần lặp	Giá trị a	sum sau khi cộng
1	4	0 + 4 = 4
2	6	4 + 6 = 10
3	8	10 + 8 = 18
📌 Kết quả in ra:

Copy
Edit
18
📌 Ví dụ 2: a = 2, b = 11
Vì 2 đã là số chẵn nên không thay đổi.
Dãy số trong range(2, 11, 2) là: 2, 4, 6, 8, 10

Lần lặp	Giá trị a	sum sau khi cộng
1	2	0 + 2 = 2
2	4	2 + 4 = 6
3	6	6 + 6 = 12
4	8	12 + 8 = 20
5	10	20 + 10 = 30
📌 Kết quả in ra:

Copy
Edit
30
🔥 Tóm lại
1️⃣ Nếu a là số lẻ, tăng a lên 1 để bắt đầu từ số chẵn.
2️⃣ Dùng for a in range(a, b, 2) để duyệt qua các số chẵn từ a đến b-1.
3️⃣ Cộng từng số chẵn vào sum.
4️⃣ In tổng các số chẵn trong khoảng [a, b).