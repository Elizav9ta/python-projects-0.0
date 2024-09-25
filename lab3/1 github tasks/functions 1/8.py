
def spy_game(nums):
    count = 0
    for num in nums:
        if num == 0:
            count += 1
        if count == 2 and num == 7:
            return True
    return False

# Example usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False