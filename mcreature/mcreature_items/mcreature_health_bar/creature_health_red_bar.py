# 빨간 체력바 클래스

import pygame
from mgame_manager.settings import *

class CreatureHealthRedBar:
    def __init__(self, healthbar):
        # 빨간 체력바 크기 조절
        self.width = healthbar.width
        self.height = healthbar.height / 2.8
        
        # 빨간 체력바 위치 조절
        self.located(healthbar)

    def located(self, healthbar):
        # 빨간 체력바 위치 조절 함수
        self.x = healthbar.x + 11.5
        self.y = healthbar.y + 11.4

    def draw(self, screen):
        # 빨간 체력바 그리기
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width * 0.8, self.height])

    def update(self, healthbar):
        # 빨간 체력바 위치 업데이트
        self.located(healthbar)