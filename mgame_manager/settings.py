# 게임을 만들 때 쓰이는 기본 변수 모음

import pygame

# 스크린 크기 관련
screen_width = 1080
screen_height = 540

# FPS
FPS = 60

# 색 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 게임 실행 관련
running = True
frame_count = 0 # 프레임 세기

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height)) # 중요