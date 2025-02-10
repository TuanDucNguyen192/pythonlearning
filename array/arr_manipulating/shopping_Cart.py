shop = ["kẹo", "bánh", "trứng", "sữa"]
cart = []
choice = 0
choose = 0
while True:
    print("==========SHOPPING CART==========")
    print("1. Xem danh sách sản phẩm")
    print("2. Xem giỏ hàng")
    print("3. Thêm sản phẩm vào giỏ hàng")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát")
    choice = int(input("Nhập lựa chọn "))
    if choice == 1:
        for i in range(len(shop)):
            print(shop[i])
    elif choice == 2:
            print("Giỏ hàng của bạn:",cart)
    elif choice == 3:
        print("Nhập sản phẩm bạn muốn thêm vào giỏ hàng ")
        for i in range(len(shop)):
            print(i + 1,":",shop[i])
        choose = int(input("Nhập số thứ tự sản phẩm bạn muốn thêm "))
        match choose:
            case 1:
                cart.append(shop[0])
            case 2:
                cart.append(shop[1])
            case 3:
                cart.append(shop[2])
            case 4:
                cart.append(shop[3])
        print(cart)
    elif choice == 4:
        print("Giỏ hàng của bạn:",cart)
        choose = int(input("Xóa số thứ tự phần tử bạn muốn "))
        match choose:
            case 1:
                cart.pop(1)
                print(cart)
            case 2:
                cart.pop(2)
                print(cart) 
            case 3:
                cart.pop(3)
                print(cart)
            case 4:
                cart.pop(4)
                print(cart)


            
            
