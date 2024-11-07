import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
player_car = pygame.image.load("car1.png")
player_car = pygame.transform.scale(player_car, (50, 100))
obstacle_car = pygame.image.load("car2.png")
obstacle_car = pygame.transform.scale(obstacle_car, (50, 100))
coin_image = pygame.image.load("coins.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))  # Scale to a smaller size
road_image = pygame.image.load("road1.png")
road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT))

# Player car setup
player_pos = [WIDTH // 2 - player_car.get_width() // 2, HEIGHT - player_car.get_height() * 2]
player_speed = 10

# Initialize score
score = 0
font = pygame.font.SysFont("monospace", 35)

# Car class for obstacles
class Car:
    def __init__(self):
        self.image = obstacle_car
        self.pos = [random.choice([WIDTH // 3 - self.image.get_width() // 2,
                                   2 * WIDTH // 3 - self.image.get_width() // 2]),
                    -self.image.get_height()]
        self.speed = random.randint(5, 10)

    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            self.pos = [random.choice([WIDTH // 3 - self.image.get_width() // 2,
                                       2 * WIDTH // 3 - self.image.get_width() // 2]),
                        -self.image.get_height()]
            self.speed = random.randint(5, 10)

    def draw(self):
        screen.blit(self.image, self.pos)

# Coin class
class Coin:
    def __init__(self):
        self.image = coin_image
        self.reset_position()

    def reset_position(self):
        self.pos = [random.choice([WIDTH // 3 - self.image.get_width() // 2,
                                   2 * WIDTH // 3 - self.image.get_width() // 2]),
                    random.randint(-HEIGHT, -self.image.get_height())]
        self.collected = False

    def move(self):
        self.pos[1] += 5  # Set a slower speed for the coins
        if self.pos[1] > HEIGHT:
            self.reset_position()

    def draw(self):
        if not self.collected:
            screen.blit(self.image, self.pos)

# Initialize cars and coins
cars = [Car() for _ in range(2)]
coins = [Coin() for _ in range(3)]  # More coins can be added if desired

# Main game loop
running = True
while running:
    screen.blit(road_image, (0, 0))  # Draw the road background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > WIDTH // 3:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < 2 * WIDTH // 3 - player_car.get_width():
        player_pos[0] += player_speed

    # Move and draw obstacle cars
    for car in cars:
        car.move()
        car.draw()
        # Collision detection between player and car
        if (player_pos[0] < car.pos[0] + car.image.get_width() and
            player_pos[0] + player_car.get_width() > car.pos[0] and
            player_pos[1] < car.pos[1] + car.image.get_height() and
            player_pos[1] + player_car.get_height() > car.pos[1]):
            print("Collision detected! Game Over.")
            pygame.quit()
            sys.exit()

    # Move and draw coins, check for collection
    for coin in coins:
        coin.move()
        coin.draw()
        # Check for collision with player
        if (player_pos[0] < coin.pos[0] + coin.image.get_width() and
            player_pos[0] + player_car.get_width() > coin.pos[0] and
            player_pos[1] < coin.pos[1] + coin.image.get_height() and
            player_pos[1] + player_car.get_height() > coin.pos[1]):
            coin.collected = True
            score += 1
            coin.reset_position()

    # Draw player car
    screen.blit(player_car, player_pos)

    # Display score in the top-right corner
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))

    pygame.display.update()
    pygame.time.Clock().tick(30)
