import math


def generate_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if number < 2:
            continue
        is_prime = True
        for divisor in range(2, math.isqrt(number) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


print("generate_primes(1, 30):", generate_primes(1, 30))
print("generate_primes(2, 2):", generate_primes(2, 2))
print("generate_primes(14, 16):", generate_primes(14, 16))
print("generate_primes(-5, 3):", generate_primes(-5, 3))
