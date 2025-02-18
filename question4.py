def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    return sum_of_powers == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

# Input from the user
num = int(input("Enter a number: "))

# Check all properties
print(f"{num} is prime: {is_prime(num)}")
print(f"{num} is perfect: {is_perfect(num)}")
print(f"{num} is Armstrong: {is_armstrong(num)}")
print(f"{num} is palindrome: {is_palindrome(num)}")
print(f"{num} is automorphic: {is_automorphic(num)}")
