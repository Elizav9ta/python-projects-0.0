import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметры змейки и еды
BLOCK_SIZE = 20
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)


clock = pygame.time.Clock()
speed = 8
score = 0
level = 1
food_counter = 0

font = pygame.font.Font(None, 36)


def game():
    global direction, food, score, level, food_counter, speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Управление направлением змейки
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

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

        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        if new_head == food:
            food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
            score += 10  # увеличиваем счет на 10
            food_counter += 1

            if food_counter == 3:
                level += 1
                speed += 2
                food_counter = 0
        else:
            snake.pop()

        snake.insert(0, new_head)

        SCREEN.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(SCREEN, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(SCREEN, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(level_text, (10, 40))

        pygame.display.flip()
        clock.tick(speed)


game()
