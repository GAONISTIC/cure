# 스킬 쿨타임을 알려주는 아이콘

import pygame
from mgame_manager.settings import *

class CreatureGrayAttackIcon:
    def __init__(self, x, y, width, height, mother_creature):
        # 위치 지정
        self.x = x
        self.y = y

        # 크기 지정
        self.width = width
        self.height = height

        # ALPHA 지정
        self.ALPHA = 128

        # 엄마 크리쳐 지정
        self.mother_creature = mother_creature

        # 초 지정
        self.seconds = 0
        self.percentage()

    # 남은 공격 딜레이 시간을 비에 맞춰 표시하는 함수
    def percentage(self):
        # seconds = (딜레이 초 - 지난 초) / (딜레이 초) * (height)
        later_seconds = self.mother_creature.b1_later_frame
        delay_seconds = self.mother_creature.b1_delay_frame

        self.seconds = (delay_seconds - later_seconds) / delay_seconds * self.height

    def draw(self, screen):
        self.percentage()

        transparent_surface = pygame.Surface((self.width, self.seconds), pygame.SRCALPHA)
        pygame.draw.rect(transparent_surface, (GRAY[0], GRAY[1], GRAY[2], self.ALPHA), transparent_surface.get_rect())

        # 투명한 Surface 그리기
        screen.blit(transparent_surface, (self.x, self.y))