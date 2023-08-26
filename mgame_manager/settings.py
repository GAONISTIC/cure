import pygame

screen_width = 1080
screen_height = 540
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
frame_count = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))