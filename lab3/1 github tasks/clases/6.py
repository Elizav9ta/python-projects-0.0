"""Write a program which can filter prime numbers in a list 
by using filter function. Note: Use lambda to define anonymous functions."""

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# List of numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 24, 29]

# Using filter and lambda to get prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# Output the filtered list of prime numbers
print("Prime numbers:", prime_numbers)
