import pygame
import mgame_manager.settings as ms

def update(screen):
    pygame.display.flip()
    ms.clock.tick(ms.FPS)
    ms.frame_count += 1

def is_QUIT():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ms.running = False

def start_game():
    pygame.init()
    pygame.display.set_caption("C.U.R.E.")

def end_game():
    pygame.quit()