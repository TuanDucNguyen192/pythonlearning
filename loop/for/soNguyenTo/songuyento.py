import math
n = int(input("Nhap so nguyen to can kiem tra "))
check = True
if n < 2:
    print("Day khong phai la so nguyen to")
else:
    for i in range (2,n,1):
        if n % i == 0:
            print("Day khong phai so nguyen to")
            check = False
            break
    if check == True:
        print("Day la so nguyen to")

