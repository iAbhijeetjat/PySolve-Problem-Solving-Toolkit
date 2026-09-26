def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def decimal_to_hex(n):
    return hex(n).replace("0x", "")