def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_square_root(n):
    return n ** 0.5

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors

def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = result * base
        base = base * base
        exp = exp // 2
    return result