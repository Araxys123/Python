# Import thu vien toan hoc
import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Phuong thuc tinh khoang cach den goc toa do

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    # Phuong thuc in toa do diem

    def print_info(self):
        print("{}, {}".format(self.x, self.y))


p1 = Point2D()
p1.print_info()
p2 = Point2D(1, 3)
p3 = Point2D(4, 5)
p2.print_info()
p3.print_info()
# Tao danh sach diem
n = int(input("Nhap so diem trong mat phang: "))
point_list = []
# Nhap toa do tung diem va dua vao danh sach
for i in range(n):
    print("Nhap diem thu {} : ". format(i + 1))
    x = int(input("x = "))
    y = int(input("y = "))
    p = Point2D(x, y)
    point_list.append(p)
# In ra danh sach cac diem da nhap
for p in point_list:
    p.print_info()
max = 0
pmax = Point2D
for p in point_list:
    if max < p.distance():
        max = p.distance()
    pmax = p
print("Diem o xa goc toa do nhat la: ")
pmax.print_info()
min_distance = float('inf')
closest_points = []

# Tìm 2 điểm gần nhau nhất trong danh sách các điểm
for i in range(len(point_list)):
    for j in range(i + 1, len(point_list)):
        distance = math.sqrt((point_list[i].x - point_list[j].x) ** 2 + (point_list[i].y - point_list[j].y) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_points = [point_list[i], point_list[j]]

# In ra 2 điểm gần nhau nhất
print("Hai diem gan nhau nhat la:")
for point in closest_points:
    point.print_info()
# Tạo một danh sách mới để lưu các điểm không trùng nhau
unique_points = []


# Duyệt qua danh sách các điểm
for p in point_list:
    # Kiểm tra xem điểm hiện tại đã tồn tại trong danh sách unique_points chưa
    if p not in unique_points:
        # Nếu chưa tồn tại, thêm điểm vào danh sách unique_points
        unique_points.append(p)

# In ra danh sách các điểm không trùng nhau
print("Danh sach cac diem khong trung nhau:")
for p in unique_points:
    p.print_info()
