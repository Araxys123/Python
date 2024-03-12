
# Tinh tong cac so nguyen
def Tong(*ds):
    s = 0
    for i in ds:
        s += i
        return s

    s = Tong(1,2,3,4)
    print(s)