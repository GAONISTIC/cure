# 게임을 만들 때 쓰이는 기본 함수 모음

import pygame
import mgame_manager.settings as ms

# 게임 업데이트 in main
def update(screen):
    pygame.display.flip()
    ms.clock.tick(ms.FPS)
    ms.frame_count += 1

# 게임 종료 확인
def is_QUIT():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ms.running = False

# 게임 시작
def start_game():
    pygame.init()
    pygame.display.set_caption("C.U.R.E.")

# 게임 종료
def end_game():
    pygame.quit()