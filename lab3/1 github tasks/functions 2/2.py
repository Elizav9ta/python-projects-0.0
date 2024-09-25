def filter_high_rated_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# Пример использования
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    # ... (другие фильмы)
]
high_rated_movies = filter_high_rated_movies(movies)
print("Movies with IMDB score above 5.5:", high_rated_movies)
