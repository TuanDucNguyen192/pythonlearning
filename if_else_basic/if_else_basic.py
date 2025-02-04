diem = 0
diem = input("nhap tuoi ")
diem = int(diem)

if diem >= 18 and diem <= 40:
    print("Ban du dieu kien tham roi")
elif diem > 40:
    print("Ban da qua tuoi de tham gia")
else:
    print("Ban chua du 18 tuoi de tham gia.")