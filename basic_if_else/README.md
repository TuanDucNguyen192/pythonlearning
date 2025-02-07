diem = int(diem)
tại sao ở đây phải để diem = int(diem)

bởi hàm input sẽ luôn lấy giá trị str nên sẽ lỗi
int(diem) thì chỉ cơ bản ra diem chứ k gán vào biến diem cũ