def is_prime(num):
    if num <= 1:
        return False  # 1 and numbers less than 1 are not prime
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:
            return False  # If the number has a divisor other than 1 and itself, it's not prime
    return True

def print_primes_and_next(n):
    print("Các số nguyên tố <= n: ", n, ":")
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
            print(num, end=" ")

    print("\nSo nguyen to nho nhat nhưng lớn hơn n: ", n, ":", end=" ")
    next_prime = n + 1
    while True:
        if is_prime(next_prime):
            print(next_prime)
            break
        next_prime += 1

if __name__ == '__main__':
    n = int(input("Enter a number: "))
print_primes_and_next(n)

