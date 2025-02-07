Số nguyên tố là số lớn hơn 2 và CHỈ chia hêt cho 1 và chính nó
nghĩa là các số sau nó đều không chia hết


Giải thích lỗi của bạn
📌 Lỗi chính:

Nếu n không phải số nguyên tố, chương trình in cả hai dòng:

print("Day khong phai so nguyen to")
print("Day la so nguyen to")  # 🚨 In sai ở đây!

→ Vì sau khi break, chương trình vẫn tiếp tục chạy dòng sau vòng lặp.
📌 Cách sửa:

Thêm biến is_prime để kiểm soát in kết quả.
Nếu tìm thấy số i nào chia hết n, gán is_prime = False và dừng vòng lặp (break).
Sau vòng lặp, nếu is_prime vẫn True, in "Day la so nguyen to".
Ví dụ chạy đúng

Nhap so nguyen to can kiem tra: 7
Day la so nguyen to

Nhap so nguyen to can kiem tra: 9
Day khong phai so nguyen to