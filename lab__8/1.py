import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Cars")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 10

class Car:
    def __init__(self):
        self.width = 50
        self.height = 80
        self.pos = [random.randint(0, WIDTH - self.width), -self.height]
        self.speed = random.randint(5, 10)

    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            self.pos = [random.randint(0, WIDTH - self.width), -self.height]
            self.speed = random.randint(5, 10)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.pos, self.width, self.height))

cars = [Car() for _ in range(5)]

font = pygame.font.SysFont("monospace", 35)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    for car in cars:
        car.move()
        car.draw()

        if (player_pos[0] < car.pos[0] + car.width and
            player_pos[0] + player_size > car.pos[0] and
            player_pos[1] < car.pos[1] + car.height and
            player_pos[1] + player_size > car.pos[1]):

            print("Collision detected! Game Over.")
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    pygame.time.Clock().tick(30)
