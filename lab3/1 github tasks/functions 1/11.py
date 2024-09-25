def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
print(is_palindrome("Madam"))  # True
print(is_palindrome("Hello"))  # False
