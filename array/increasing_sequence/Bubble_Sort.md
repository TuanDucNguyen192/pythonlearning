Bubble Sort là một thuật toán sắp xếp đơn giản. Nó so sánh từng cặp phần tử liền kề và hoán đổi chúng nếu chúng không theo thứ tự mong muốn. Sau mỗi vòng lặp, phần tử lớn nhất sẽ được "nổi lên" cuối mảng.

Cách Bubble Sort hoạt động:
Duyệt qua dãy số.
So sánh các phần tử liền kề và hoán đổi chúng nếu phần tử bên trái lớn hơn phần tử bên phải.
Lặp lại cho đến khi không còn phần tử nào cần hoán đổi.
Mã nguồn Bubble Sort:
python
Copy
Edit
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi phần tử
    return arr

arr = [64, 25, 12, 22, 11]
print("Bubble Sort:", bubble_sort(arr))
Giải thích:
Quá trình: Các phần tử sẽ được so sánh lần lượt. Sau mỗi vòng lặp, phần tử lớn nhất sẽ được đưa vào cuối mảng.
Độ phức tạp: O(n²) (trong trường hợp xấu nhất).