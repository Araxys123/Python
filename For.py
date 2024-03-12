fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

personal_info = {'Name': 'Hoang',
                 'Tuoi': 17,
                 'Chieucao': 170,
                 'Cannang':68}
# Lap 1 bien chay
for i in personal_info.items():
    print(i)

# Lap 2 bien chay
for k, v in personal_info.items():
    print(k, v)

# Lenh lap for voi ham range():
# VD1: In ra cac so nguyen lien tiep tu 0 ... (n-1)
# for i in range (n)
# print(i)

# Xet cac so trong khoang gia tri:
# for i in range (start, end, step)
for i in range(1, 6, 2):
    print(i)

n = 10
myNum = range(n)
for i in myNum:
    print(i, end=' ')
for i in range(1, n, 2):
    print(i)
for i in range(0, n, 2):
    print(i)
