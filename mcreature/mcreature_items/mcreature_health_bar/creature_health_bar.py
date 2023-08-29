# 크리쳐 체력바 클래스

import pygame
from mcreature.mcreature_items.mcreature_health_bar.creature_health_red_bar import CreatureHealthRedBar

class CreatureHealthBar:
    def __init__(self, mother_creature):
        # 부모 클래스 지정
        self.mother_creature = mother_creature
        
        # 체력 지정
        self.max_health = self.mother_creature.health # 최대 체력
        self.now_health = self.mother_creature.health # 현재 체력
        # 체력을 백분율로 나누어 저장
        self.set_percent_health()

        # 위치 지정
        self.x = self.mother_creature.x
        self.y = self.mother_creature.y - self.mother_creature.height / 3
        
        # 크기 지정
        self.width = mother_creature.width
        self.height = mother_creature.height / 3

        # 파일 지정
        self.filepath = "C:/Users/freeg/Desktop/cure/assets/health_bar.png"

        # 이미지 파일 불러오기
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        # 위치 지정
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        # 빨간 체력바 지정
        self.red_bar = CreatureHealthRedBar(self)

    # 체력 백분율
    def set_percent_health(self):
        self.percent_health = (self.now_health / self.max_health) * 100

    def draw(self, screen):
        # 체력바 그리기
        screen.blit(self.image, self.rect.topleft)
        self.red_bar.draw(screen) # 빨간 체력바 그리기

    def update(self):
        # 체력바 위치 업데이트
        self.x = self.mother_creature.x
        self.y = self.mother_creature.y - self.mother_creature.height / 3
        self.rect.topleft = (self.x, self.y)
        self.now_health = self.mother_creature.health

        # 체력 업데이트
        self.set_percent_health()

        # 빨간 체력바 길이 조절
        self.red_bar.width = self.percent_health
        self.red_bar.update(self)