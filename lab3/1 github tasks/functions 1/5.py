import itertools

def print_permutations(s):
    permutations = itertools.permutations(s)
    for perm in permutations:
        print(''.join(perm))

# Example usage:
user_input = input("Enter a string: ")
print_permutations(user_input)
