def is_high_rating(movie):
    return movie['imdb'] > 5.5

# Пример использования
movie = {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}
print(is_high_rating(movie))  # True
