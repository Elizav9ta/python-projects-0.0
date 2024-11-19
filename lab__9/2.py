import pygame
import random
import sys

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Размер блока
BLOCK_SIZE = 20

# Начальная змейка
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'

# Таймер для исчезающих продуктов
food_timer = 0
max_food_time = 300  # Максимальное время жизни еды (в тиках)

# Создание еды с разными типами (весами)
food_types = [
    {"color": RED, "weight": 10},     # Красная еда: 10 очков
    {"color": YELLOW, "weight": 20},  # Желтая еда: 20 очков
]
food = {
    "position": (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                 random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE),
    "type": random.choice(food_types)
}

# Игровые параметры
clock = pygame.time.Clock()
speed = 8
score = 0
level = 1
food_counter = 0

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Функция запуска игры
def game():
    global direction, food, score, level, food_counter, speed, food_timer

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Завершение игры
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Управление направлением змейки
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Движение змейки
        x, y = snake[0]
        if direction == 'UP':
            y -= BLOCK_SIZE
        elif direction == 'DOWN':
            y += BLOCK_SIZE
        elif direction == 'LEFT':
            x -= BLOCK_SIZE
        elif direction == 'RIGHT':
            x += BLOCK_SIZE
        new_head = (x, y)

        # Проверка на столкновение с границами или телом змейки
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Проверка на поедание еды
        if new_head == food["position"]:
            score += food["type"]["weight"]  # Увеличиваем счет на вес текущей еды
            food_counter += 1

            # Увеличиваем уровень и скорость каждые 3 съеденные еды
            if food_counter == 3:
                level += 1
                speed += 2
                food_counter = 0

            # Генерация новой еды
            food = {
                "position": (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                             random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE),
                "type": random.choice(food_types)
            }
            food_timer = 0  # Сброс таймера еды
        else:
            snake.pop()  # Если еда не съедена, убираем хвост змейки

        # Добавляем новую голову
        snake.insert(0, new_head)

        # Увеличение таймера еды
        food_timer += 1
        if food_timer >= max_food_time:  # Если еда "стареет", она исчезает и появляется новая
            food = {
                "position": (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                             random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE),
                "type": random.choice(food_types)
            }
            food_timer = 0  # Сброс таймера еды

        # Очистка экрана
        SCREEN.fill(BLACK)

        # Отрисовка змейки
        for segment in snake:
            pygame.draw.rect(SCREEN, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

        # Отрисовка еды
        pygame.draw.rect(SCREEN, food["type"]["color"], (*food["position"], BLOCK_SIZE, BLOCK_SIZE))

        # Отрисовка текста (счет и уровень)
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(level_text, (10, 40))

        # Обновление экрана и управление частотой кадров
        pygame.display.flip()
        clock.tick(speed)

game()
