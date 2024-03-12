def atm_withdrawal(amount):
    denominations = [100, 20, 5]  # Danh sách các mệnh giá tiền
    min_bills = float('inf')  # Số tờ tiền tối thiểu cần để rút số tiền cần thiết
    min_combinations = []  # Danh sách các kết hợp tiền ít tờ nhất

    # Hàm đệ quy để tìm các kết hợp tiền
    def find_combinations(total, combination, idx):
        nonlocal min_bills, min_combinations

        if total == amount:  # Nếu tổng tiền đạt đúng số tiền cần rút
            nonlocal min_bills, min_combinations
            num_bills = sum(combination)  # Tính tổng số tờ tiền trong kết hợp
            if num_bills < min_bills:  # Nếu số tờ tiền nhỏ hơn số tờ tiền tối thiểu đã tìm được trước đó
                min_bills = num_bills  # Cập nhật số tờ tiền tối thiểu
                min_combinations = [combination[:]]  # Cập nhật danh sách kết hợp mới
            elif num_bills == min_bills:  # Nếu số tờ tiền bằng số tờ tiền tối thiểu đã tìm được trước đó
                min_combinations.append(combination[:])  # Thêm kết hợp vào danh sách

        for i in range(idx, len(denominations)):  # Duyệt qua các mệnh giá tiền
            if total + denominations[i] <= amount:  # Nếu tổng tiền sau khi thêm mệnh giá tiền không vượt quá số tiền cần rút
                combination.append(denominations[i])  # Thêm mệnh giá tiền vào kết hợp
                find_combinations(total + denominations[i], combination, i)  # Gọi đệ quy với tổng tiền mới
                combination.pop()  # Loại bỏ mệnh giá tiền để thử các kết hợp khác

    find_combinations(0, [], 0)  # Gọi hàm tìm kết hợp với tổng tiền hiện tại là 0

    if not min_combinations:  # Nếu không có kết hợp nào
        print("Không thể rút số tiền này.")  # In thông báo lỗi
    else:
        print("Phương án rút tiền tốt nhất:")  # In tiêu đề phương án tốt nhất
        for combination in min_combinations:  # Duyệt qua các kết hợp
            print(combination)  # In từng kết hợp

# Nhập số tiền cần rút từ người dùng
amount = int(input("Nhập số tiền cần rút: "))
atm_withdrawal(amount)  # Gọi hàm rút tiền với số tiền đã nhập

