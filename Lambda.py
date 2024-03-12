import numpy

s = 0
n = 5
for i in range(n + 1):
    s += lambda i: i ** 2
    print('S = {}'.format(s))

for i in range(n + 1):
    s += numpy.square(i)
    print('S = {}'.format(s))

for i in range(n + 1):
    s = lambda i: i*i
    s += x(i)

