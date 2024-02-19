def duong_lunar(nam):
    duong_lunar = {
        0: "Canh",
        1: "Tân",
        2: "Nhâm",
        3: "Quý",
        4: "Giáp",
        5: "Ất",
        6: "Bính",
        7: "Đinh",
        8: "Mậu",
        9: "Kỷ"
    }

    chi_lunar = {
        0: "Thân",
        1: "Dậu",
        2: "Tuất",
        3: "Hợi",
        4: "Tý",
        5: "Sửu",
        6: "Dần",
        7: "Mão",
        8: "Thìn",
        9: "Tỵ",
        10: "Ngọ",
        11: "Mùi"
    }

    can_index = nam % 10
    chi_index = nam % 12

    can = duong_lunar[can_index]
    chi = chi_lunar[chi_index]

    return f"{can} {chi}"

nam_duong = int(input("Nhập năm dương lịch: "))
nam_am = duong_lunar(nam_duong)
print(f"Năm âm lịch tương ứng là: {nam_am}")
