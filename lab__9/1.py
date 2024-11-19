import pygame
import random
import sys

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гоночная игра с монетами")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Загрузка ресурсов
road_image = pygame.image.load("road1.png")
road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT))
player_car = pygame.image.load("car1.png")
player_car = pygame.transform.scale(player_car, (50, 100))
obstacle_car = pygame.image.load("car2.png")
obstacle_car = pygame.transform.scale(obstacle_car, (50, 100))
coin_image1 = pygame.image.load("coins.png")
coin_image1 = pygame.transform.scale(coin_image1, (30, 30))
coin_image2 = pygame.image.load("coins 2.png")
coin_image2 = pygame.transform.scale(coin_image2, (30, 30))
crash_sound = pygame.mixer.Sound("crash.wav")

# Шрифты
font = pygame.font.SysFont("monospace", 35)
game_over_font = pygame.font.SysFont("Verdana", 60)

# Параметры игрока
player_pos = [WIDTH // 2 - player_car.get_width() // 2, HEIGHT - player_car.get_height() * 2]
player_speed = 10

# Счет
score = 0
coins_collected = 0
speed = 5

# Классы объектов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_car
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([WIDTH // 3, 2 * WIDTH // 3]), -self.rect.height)
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.center = (random.choice([WIDTH // 3, 2 * WIDTH // 3]), -self.rect.height)
            global score
            score += 1


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice([1, 2])
        self.image = coin_image1 if self.type == 1 else coin_image2
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([WIDTH // 3, 2 * WIDTH // 3]), -self.rect.height)
        self.weight = 1 if self.type == 1 else 2

    def update(self):
        self.rect.y += speed
        if self.rect.top > HEIGHT:
            self.kill()


# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Создание начальных объектов
player = pygame.sprite.Sprite()
player.image = player_car
player.rect = player.image.get_rect()
player.rect.center = player_pos
all_sprites.add(player)

for _ in range(2):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

for _ in range(3):
    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)

# Игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    screen.blit(road_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.left > WIDTH // 3:
        player.rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player.rect.right < 2 * WIDTH // 3:
        player.rect.x += player_speed

    # Проверка столкновений
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        screen.fill(RED)
        game_over_text = game_over_font.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Сбор монет
    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    for coin in collected_coins:
        coins_collected += coin.weight

    # Увеличение скорости
    if coins_collected >= 10:
        speed += 0.5

    # Создание новых монет
    if random.randint(1, 100) > 98:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Обновление всех спрайтов
    all_sprites.update()

    # Отрисовка
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, WHITE)
    coins_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (WIDTH - 200, 10))

    pygame.display.update()
    clock.tick(30)
