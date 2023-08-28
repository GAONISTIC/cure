# 플레이어의 공격 아이콘 (쿨타임 등을 표시)

import pygame
from mcreature.mcreature_items.mcreature_attack_icon.mcreature_gray_attack_icon import CreatureGrayAttackIcon

class CreatureAttackIcon:
    def __init__(self, icontype, mother_creature): # icontype is 어택 아이콘의 종류
        # 위치 지정
        self.x = 25
        self.y = 465

        # 크기 지정
        self.width = 50
        self.height = 50

        # 이미지 지정
        self.filepath = f"C:/Users/freeg/Desktop/cure/assets/player_{icontype}_icon.png"
        
        # 이미지 파일 불러오기
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        # 위치 지정
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        # 엄마 크리쳐 지정
        self.mother_creature = mother_creature  

        # 회색 공격 아이콘 지정
        self.grayIcon = CreatureGrayAttackIcon(self.x, self.y, self.width, self.height, self.mother_creature)


    def draw(self, screen):
        # 공격 아이콘 그리기
        screen.blit(self.image, self.rect.topleft)
        self.grayIcon.draw(screen)