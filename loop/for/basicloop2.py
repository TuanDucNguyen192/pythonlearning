a = int(input("Nhap so nguyen a "))
b = int(input("Nhap so nguyen b "))
sum = 0
if a % 2 != 0:
    a +=1
for a in range(a,b,2):
    sum+=a
print(sum)