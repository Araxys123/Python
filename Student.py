# Cai dat lop Student mo ta cac doi tuong sinh vien
class Student:
    # Khai bao cac thuoc tinh
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        # Ham in thong tin
    def print_info(self):
        print("ID: " + self.id)
        print("Name: " + self.name)
        print("Grade: " + str(self.grade))

# Khoi tao 1 doi tuong sinh vien
sv1 = Student("63136363", "Le Van Hoa", 8.88)
print(sv1.id)
print(sv1.name)
print(sv1.grade)
sv1.print_info()
