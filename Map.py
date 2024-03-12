# Cach 1
a = [1, 2, 3, 4]
b = []
for i in range(len(a)):
    b.append(a[i] ** 2)
    print(b)

# Cach 2
def Square(x):
    return x ** 2
b = map(Square, a)
b = list(b)
print(b)

b = list(map(lambda x: x ** 2, a))
print(b)
