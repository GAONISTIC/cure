# 세계 관리 업데이트

from mscreen.screen_set import Screen_set
import mgame_manager.settings as ms
import pygame

class Screen:
    def __init__(self):
        # 현재 세계 지정
        self.world = Screen_set.NORMAL_WORLD.value

        self.bgpath = "C:/Users/freeg/Desktop/cure/assets/planet0bg.png"
        self.bg = pygame.image.load(self.bgpath)

        self.bg = pygame.transform.scale(self.bg, (1080, 540))

    def change_world(self):
        # 짝수면 깨어진 세계임
        self.world += 1

    def screen_fill(self, screen):
        if self.world % 2 == Screen_set.BROKEN_WORLD.value:
            screen.fill(ms.BLACK)

        elif self.world % 2 == Screen_set.NORMAL_WORLD.value:
            screen.fill(ms.WHITE)

    def screen_fill_bg(self, screen):
        screen.blit(self.bg, (0, 0))