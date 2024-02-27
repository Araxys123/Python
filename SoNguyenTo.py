def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_less_than_n(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Nhập n: "))
if 0 < n <= 1000:
    print("Các số nguyên tố bé hơn n là:", primes_less_than_n(n))
else:
    print("n phải thoả điều kiện 0 < n <= 1000")

# def LaSNT (n):
    # if n < 2:
    #  return False
    # for i in range (2, n//2 + 1)
    # if n % i = 0:
    # return False
    # return True

#a KTSNT:
# if LaSNT (n):
# print("() là số nguyên tố", format(n))
# else
# print("() không là số nguyên tố", format(n))

#b In ra các số SNT bé hơn n
# print("Các số nguyên tố <= ()", format(n))
# for i in range (2, n+1):
# print ("%5d" % i, end:" ")

