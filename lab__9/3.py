import pygame
import sys

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

# Параметры кисти и начальной фигуры
brush_size = 5
shape = 'brush'

# Заливка фона белым цветом
screen.fill(WHITE)

# Функции для рисования
def draw_rectangle(start_pos, end_pos, color):
    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    pygame.draw.rect(screen, color, rect, 2)

def draw_circle(start_pos, end_pos, color):
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 // 2)
    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
    pygame.draw.circle(screen, color, center, radius, 2)

def draw_square(start_pos, end_pos, color):
    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
    pygame.draw.rect(screen, color, rect, 2)

def draw_right_triangle(start_pos, end_pos, color):
    points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
    pygame.draw.polygon(screen, color, points, 2)

def draw_equilateral_triangle(start_pos, end_pos, color):
    base = abs(end_pos[0] - start_pos[0])
    height = int((3 ** 0.5 / 2) * base)  # Высота равностороннего треугольника
    if start_pos[1] + height > HEIGHT:
        height = HEIGHT - start_pos[1]
    center_x = (start_pos[0] + end_pos[0]) // 2
    points = [
        (center_x, start_pos[1]),
        (start_pos[0], start_pos[1] + height),
        (end_pos[0], start_pos[1] + height)
    ]
    pygame.draw.polygon(screen, color, points, 2)

def draw_rhombus(start_pos, end_pos, color):
    center_x = (start_pos[0] + end_pos[0]) // 2
    center_y = (start_pos[1] + end_pos[1]) // 2
    points = [
        (center_x, start_pos[1]),  # Верхний угол
        (end_pos[0], center_y),   # Правый угол
        (center_x, end_pos[1]),   # Нижний угол
        (start_pos[0], center_y)  # Левый угол
    ]
    pygame.draw.polygon(screen, color, points, 2)

def draw_eraser(pos, size):
    pygame.draw.circle(screen, WHITE, pos, size)

# Управление рисованием
drawing = False
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                shape = 'brush'
            elif event.key == pygame.K_r:
                shape = 'rectangle'
            elif event.key == pygame.K_s:
                shape = 'square'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_t:
                shape = 'right_triangle'
            elif event.key == pygame.K_e:
                shape = 'equilateral_triangle'
            elif event.key == pygame.K_d:
                shape = 'rhombus'
            elif event.key == pygame.K_e:
                shape = 'eraser'
            elif event.key == pygame.K_1:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_2:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_3:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_4:
                current_color = (0, 0, 0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and shape in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                end_pos = event.pos
                if shape == 'rectangle':
                    draw_rectangle(start_pos, end_pos, current_color)
                elif shape == 'circle':
                    draw_circle(start_pos, end_pos, current_color)
                elif shape == 'square':
                    draw_square(start_pos, end_pos, current_color)
                elif shape == 'right_triangle':
                    draw_right_triangle(start_pos, end_pos, current_color)
                elif shape == 'equilateral_triangle':
                    draw_equilateral_triangle(start_pos, end_pos, current_color)
                elif shape == 'rhombus':
                    draw_rhombus(start_pos, end_pos, current_color)
            drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if shape == 'brush':
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)
                elif shape == 'eraser':
                    draw_eraser(event.pos, brush_size)

    pygame.display.flip()
