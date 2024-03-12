while True:
    m = int(input("Nhap so tien rut: "))
    if m <= 0 and m % 5 != 0:
        print("So tien khong thoa man")
    else: break
m1 = m
soTo100 = m // 100 # Chia lay phan nguyen
m = m % 100        # So tien con lai
soTo20 = m // 20
m = m % 20
soTo5 = m // 5
print("Phuong an rut tien tot nhat: ")
print('{} to 100 + {} to 20 + {} to 5'.format(soTo100, soTo20, soTo5))
m = m1
soCach = 0
for soTo100 in range(m // 100 + 1):
    for soTo20 in range(m // 20 + 1):
        for soTo5 in range(m // 5 + 1):
            if soTo5*5 + soTo20*20 + soTo100*100 == m:
                soCach += 1
                print('{}: {} to 100 + {} to 20 + {} to 5'.format(soCach, soTo100, soTo20, soTo5))
