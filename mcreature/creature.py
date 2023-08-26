# 크리쳐 클래스

import pygame
import mcreature.creature_move as cmove
import mcreature.creature_attack as cattack

class Creature:
    def __init__(self, name, health, power, defense, speed, width, height, x, y, jumpSize, filepath):
        # 기본 변수들        
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # 점프 관련 변수
        self.jumpSize = jumpSize
        self.isJumping = False
        self.jumpingOrNot = 0
        self.nowy = y
        self.jumpK = 1.1

        # 움직임 관련 변수
        self.isRunning = False
        self.speed = speed
        self.max_speed = speed
        self.left_or_right = "none"
        self.sliding_speed = 0.4

        # 기본 이미지 설정
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        # 크리쳐 그리기
        screen.blit(self.image, self.rect.topleft)

    def move(self):
        # 크리쳐 움직이기 (순수 가상 함수)
        self.rect.topleft = (self.x, self.y)
        pygame.display.update()

    def update(self):
        # 움직이고 점프를 같이 함
        self.move()
        cmove.jump(self)

    def only_jump(self):
        # 플레이어 클래스는 움직임 함수가 따로 있으므로 점프만^^
        cmove.jump(self)