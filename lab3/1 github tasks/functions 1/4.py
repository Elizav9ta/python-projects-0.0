"""You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument 
and returns only prime numbers from the list."""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

# Example usage:
input_numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
primes = filter_prime(input_numbers)
print("Prime numbers:", primes)
