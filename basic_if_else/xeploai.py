x = int(input("Nhap diem "))
if x >= 8:
    print("Loai Gioi")
elif x >= 6.5 and x < 8:
    print("Loai Kha")
elif x >= 5 and x < 6.5:
    print("Trung Binh")
else:
    print("Yeu")