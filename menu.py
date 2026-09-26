from fundamental_algorithms import factorial, fibonacci, reverse_number, decimal_to_binary, decimal_to_octal, decimal_to_hex
from number_theory import gcd, is_prime, find_square_root, prime_factors, power
from array_operations import reverse_array, find_max, remove_duplicates, find_kth_smallest, demonstrate_data_structures


def module1_menu():
    while True:
        print("\n--- MODULE 1: Fundamental Algorithms ---")
        print("1. Factorial")
        print("2. Fibonacci Sequence")
        print("3. Reverse a Number")
        print("4. Base Conversion (Binary/Octal/Hex)")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print("Factorial of", num, "is", factorial(num))
        elif choice == "2":
            terms = int(input("How many Fibonacci terms? "))
            print("Fibonacci sequence:", fibonacci(terms))
        elif choice == "3":
            num = int(input("Enter a number: "))
            print("Reversed number:", reverse_number(num))
        elif choice == "4":
            num = int(input("Enter a number: "))
            print("Binary:", decimal_to_binary(num))
            print("Octal:", decimal_to_octal(num))
            print("Hexadecimal:", decimal_to_hex(num))
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def module2_menu():
    while True:
        print("\n--- MODULE 2: Number Theory Tools ---")
        print("1. GCD of two numbers")
        print("2. Check if Prime")
        print("3. Square Root")
        print("4. Prime Factors")
        print("5. Power of a Number")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD is", gcd(a, b))
        elif choice == "2":
            n = int(input("Enter a number: "))
            print(n, "is prime:", is_prime(n))
        elif choice == "3":
            n = float(input("Enter a number: "))
            print("Square root is", find_square_root(n))
        elif choice == "4":
            n = int(input("Enter a number: "))
            print("Prime factors:", prime_factors(n))
        elif choice == "5":
            base = int(input("Enter base: "))
            exp = int(input("Enter exponent: "))
            print(base, "^", exp, "=", power(base, exp))
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def module3_menu():
    while True:
        print("\n--- MODULE 3: Array & Data Structure Lab ---")
        print("1. Reverse an Array")
        print("2. Find Maximum Number")
        print("3. Remove Duplicates")
        print("4. Find Kth Smallest Element")
        print("5. List/Tuple/Set/Dictionary Demo")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Reversed array:", reverse_array(arr))
        elif choice == "2":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Maximum number:", find_max(arr))
        elif choice == "3":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Array without duplicates:", remove_duplicates(arr))
        elif choice == "4":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            k = int(input("Enter K: "))
            print("Kth smallest element:", find_kth_smallest(arr, k))
        elif choice == "5":
            demonstrate_data_structures()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def main_menu():
    while True:
        print("\n========================================")
        print(" Welcome to PySolve - Problem Solving Toolkit")
        print("========================================")
        print("1. Fundamental Algorithms")
        print("2. Number Theory Tools")
        print("3. Array & Data Structure Lab")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            module1_menu()
        elif choice == "2":
            module2_menu()
        elif choice == "3":
            module3_menu()
        elif choice == "0":
            print("Thank you for using PySolve. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")