import random
import math

def is_prime(n):
    if n < 2:
        return False
    small_primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    if n in small_primes:
        return True
    for p in small_primes:
        if n % p == 0:
            return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small_primes:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def random_prime(bits):
    while True:
        n = random.getrandbits(bits)
        n |= (1 << (bits - 1)) | 1
        if is_prime(n):
            return n
        
MERSENNE_10 = (1 << 89) - 1

def largest_primes_below_mersenne():
    result = []
    n = MERSENNE_10 - 1
    while len(result) < 10:
        if is_prime(n):
            result.append(n)
        n -= 1
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_exp(a, x, p):
    return pow(a, x, p)

if __name__ == "__main__":
    print("Tạo số nguyên tố ngẫu nhiên: ")
    print("8-bit:", random_prime(8))
    print("16-bit:", random_prime(16))
    print("64-bit:", random_prime(64))

    print("\n10 số nguyên tố lớn nhất < 2^89 - 1")
    for i, p in enumerate(largest_primes_below_mersenne(), 1):
        print(f"{i}: {p}")

    print("\nKiểm tra nguyên tố: ")
    n = int(input("Nhập số (< 2^89): "))
    if n >= MERSENNE_10:
        print("Số vượt quá giới hạn đề bài")
    else:
        print("Số " + str(n) + " là nguyên tố" if is_prime(n) else "Số " + str(n) + " là hợp số")

    print("\nGCD số lớn: ")
    a = int(input("a = "))
    b = int(input("b = "))
    print("gcd =", gcd(a, b))

    print("\nLũy thừa module:")
    a = int(input("a = "))
    x = int(input("x = "))
    p = int(input("p = "))
    print("a^x mod p =", mod_exp(a, x, p))