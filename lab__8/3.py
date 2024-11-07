import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

brush_size = 5
shape = 'brush'

screen.fill(WHITE)

def draw_rectangle(start_pos, end_pos, color):
    rect_width = end_pos[0] - start_pos[0]
    rect_height = end_pos[1] - start_pos[1]
    pygame.draw.rect(screen, color, pygame.Rect(start_pos, (rect_width, rect_height)), 2)

def draw_circle(start_pos, end_pos, color):
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
    pygame.draw.circle(screen, color, center, radius, 2)

def draw_eraser(pos, size):
    pygame.draw.circle(screen, WHITE, pos, size)

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
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_e:
                shape = 'eraser'
            elif event.key == pygame.K_1:
                current_color = (255, 0, 0)  # Red
            elif event.key == pygame.K_2:
                current_color = (0, 255, 0)  # Green
            elif event.key == pygame.K_3:
                current_color = (0, 0, 255)  # Blue
            elif event.key == pygame.K_4:
                current_color = (0, 0, 0)    # Black

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and shape in ['rectangle', 'circle']:
                end_pos = event.pos
                if shape == 'rectangle':
                    draw_rectangle(start_pos, end_pos, current_color)
                elif shape == 'circle':
                    draw_circle(start_pos, end_pos, current_color)
            drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if shape == 'brush':
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)
                elif shape == 'eraser':
                    draw_eraser(event.pos, brush_size)

    pygame.display.flip()
