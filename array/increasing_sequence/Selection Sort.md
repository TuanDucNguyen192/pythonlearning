[23, 2, 34, 5,  1,  6]
 0   1  2   3   4   5 
mục đích là chia thành 2 đoạn

ban đầu dựa vào index
tạo vòng lặp từ 0 - > 6 => bởi trong python range(0,6) như i=0,i<6

for i in range (6):
    min = i
    for j in range(i + 1, 6):
  
 
tại i = 0
xđ min = 23
lặp một vòng compare 23 với các số khác 
nếu nhỏ hơn 23 thì swap
if arr[j]  < arr[min]:
min = j // lưu index bởi min là index nếu để arr[j] giá trị sẽ sai

--> nếu duyệt hết và tìm đc min thì swap
swap ptu tử tại min đó với arr tại i
temp = arr[i]
arr[i] = arr[min]
arr[min] = arr[i]

