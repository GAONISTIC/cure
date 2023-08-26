# 무기 클래스

import pygame
import assets.functions as af
from mweapon.weapon_keys import WeaponKey
import mweapon.weapon_motions as wmotion

class Weapon:
    def __init__(self, name, power, width, height, x, y):
        # 기본적인 변수 설정
        self.name = name
        self.power = power
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # 공격 모션 설정
        self.start_attack_frame = 0
        self.delay_attack_frame = 5
        self.is_attacking = False

        # 기본 이미지 설정
        self.image = pygame.image.load(af.find_weapon_image_directory("basic", "none"))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        # 무기 그리기
        screen.blit(self.image, self.rect.topleft)

    def move(self, parents_creature):
        # 무기 움직임
        keys = pygame.key.get_pressed()

        # B1 공격
        if keys[WeaponKey.ATT_B1.value]:
            print("B1ATTACK WITH WEAPON")
            wmotion.B1ATTACK_motion(self)
            
        # B2 공격
        if keys[WeaponKey.ATT_B2.value]:
            print("B2ATTACK WITH WEAPON")
            
        # CM 공격
        if keys[WeaponKey.ATT_CM.value]:
            print("CMATTACK WITH WEAPON")
            
        # S1 공격
        if keys[WeaponKey.ATT_S1.value]:
            print("S1ATTACK WITH WEAPON")
            
        # S2 공격
        if keys[WeaponKey.ATT_S2.value]:
            print("S2ATTACK WITH WEAPON")

        # 움직임 관리
        wmotion.checking_motion(self)

        if self.is_attacking == False:
            self.x = parents_creature.x + self.width
        self.y = parents_creature.y - self.height / 5
        self.rect.topleft = (self.x, self.y)
        pygame.display.update()

    def update(self, parent_player):
        # 무기 업데이트
        self.move(parent_player)