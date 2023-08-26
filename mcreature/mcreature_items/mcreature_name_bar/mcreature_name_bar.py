# 크리쳐의 이름을 표기하기 위한 클래스

import pygame
from mgame_manager.settings import *

class CreatureNameBar:
    def __init__(self, mother_creature):
        # 부모 크리쳐 지정
        self.mother_creature = mother_creature
        self.name = self.mother_creature.name

        # 초기 위치 지정
        self.x = self.mother_creature.x + self.mother_creature.width / 2.7
        self.y = self.mother_creature.y - self.mother_creature.height / 3

    def draw(self, screen):
        # 텍스트 생성
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.name, True, BLACK)

        screen.blit(text_render, (self.x, self.y))

    def update(self):
        # 이름 바의 위치 바꾸기
        self.x = self.mother_creature.x + self.mother_creature.width / 2.7
        self.y = self.mother_creature.y - self.mother_creature.height / 2