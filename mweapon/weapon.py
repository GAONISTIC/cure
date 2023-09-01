# 무기 클래스

import pygame
import assets.functions as af
from mweapon.weapon_keys import WeaponKey
import mweapon.weapon_motions as wmotion
from mweapon.weapon_attack import *

class Weapon:
    def __init__(self, name, power, width, height, x, y, player, mother_creature):
        # 기본적인 변수 설정
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.mother_creature = mother_creature
        self.power = self.mother_creature.power

        # 공격 모션 설정
        self.start_attack_frame = 0
        self.delay_attack_frame = 50
        self.is_attacking = False

        # 기본 이미지 설정
        self.image = pygame.image.load(af.find_weapon_image_directory("basic", "none"))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        # 플레이어 설정
        self.player = player

        # 공격 딜레이에 따른 모션 딜레이 설정(한 번만 모션이 나오게)
        self.is_motioning = False # False일때 True로 바꾸고 한 번만 실행. 공격이 끝나면 다시 False로

        # 너 내 동료가 되라 (로봇 피격상태 저장)
        self.save_attacked_robot = []

    def draw(self, screen):
        # 무기 그리기
        screen.blit(self.image, self.rect.topleft)

    def move(self, parents_creature, robot_manager):
        # 무기 움직임
        keys = pygame.key.get_pressed()

        # B1 공격
        if keys[WeaponKey.ATT_B1.value]:
            # print("B1ATTACK WITH WEAPON")

            # 공격이 시작할 때 딱 한 번만 모션이 취해지게
            if self.player.b1_is_attacking and self.is_motioning == False:
                wmotion.B1ATTACK_motion(self)
                # 다시 모션이 나오지 않게 True로 
                self.is_motioning = True
            
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

        # 원래 위치로 가기
        if self.is_attacking == False:
            self.x = parents_creature.x + self.width
        self.y = parents_creature.y - self.height / 5
        self.rect.topleft = (self.x, self.y)

        # 공격이 끝나면 다시 False로 바꿔서 모션을 다시 취할 수 있게
        if self.player.b1_is_attacking == False:
            self.is_motioning = False
            self.save_attacked_robot = []

        if self.player.b1_is_attacking == True:
            is_robot_attacked(self, robot_manager)

    def update(self, parent_player, robot_manager):
        # 무기 업데이트
        self.move(parent_player, robot_manager)