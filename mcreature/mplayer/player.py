# 플레이터 클래스

from mcreature.creature import Creature
import mcreature.creature_move as cmove
import mcreature.mplayer.player_attack as pattack
from mcreature.mplayer.player_keys import PlayerKey
import assets.functions as af
import pygame

class Player(Creature):
    def __init__(self, name, health, power, defense, speed, width, height, x, y, jumpSize, playerType):
        filepath = af.find_player_image_directory("basic", "gravity")
        super().__init__(name, health, power, defense, speed, width, height, x, y, jumpSize, filepath)
        
        # 속성
        self.playerType = playerType

        # 딜레이 관련
        self.b1_delay_frame = 100
        self.b1_later_frame = 0
        self.b1_is_attacking = False

    def set_gravity(self, gravity):
        self.gravity = gravity

    def move(self, game_screen):
        keys = pygame.key.get_pressed()

        # 움직이지 않았다면 슬라이딩 실행
        move = False

        # 왼쪽 움직임
        if keys[PlayerKey.MOVE_LEFT.value]:
            cmove.move_left(self)

            # 슬라이딩 관련
            move = True
            self.left_or_right = "left"

        # 오른쪽 움직임
        if keys[PlayerKey.MOVE_RIGHT.value]:
            cmove.move_right(self)

            # 슬라이딩 관련
            move = True
            self.left_or_right = "right"

        # 점프 움직임
        if keys[PlayerKey.MOVE_JUMP.value]:
            # 점프 CHECK
            cmove.set_is_jumping(self)

        # 숙이기 움직임
        if keys[PlayerKey.MOVE_DOWN.value]:
            cmove.down(self)

        # B1 공격(Basic 1)
        if keys[PlayerKey.ATT_B1.value]:
            if self.b1_is_attacking == False:
                self.b1_is_attacking = True
                self.b1_later_frame = 0
                pattack.B1_ATTACK()

        # B2 공격(Basic 2)
        if keys[PlayerKey.ATT_B2.value]:
            pattack.B2_ATTACK()

        # CM 공격(COMBO)
        if keys[PlayerKey.ATT_CM.value]:
            pattack.CM_ATTACK()

        # S1 공격(Super 1)
        if keys[PlayerKey.ATT_S1.value]:
            pattack.S1_ATTACK()
            self.gravity.move(1)

        # S2 공격(Super 2)
        if keys[PlayerKey.ATT_S2.value]:
            pattack.S2_ATTACK()
            self.gravity.move(-1)

        # 깨어진 세계 입장
        if keys[PlayerKey.BROKEN_WORLD.value]:
            game_screen.change_world()

        # 움직이지 않았다면(움직임: 왼쪽 or 오른쪽)
        if move == False:
            # 슬라이딩 하기
            cmove.sliding(self)

        # 위치 조정
        self.rect.topleft = (self.x, self.y)

        if self.b1_is_attacking == True:
            self.b1_later_frame += 1

        if self.b1_later_frame > self.b1_delay_frame:
            self.b1_is_attacking = False

    # 플레이어 업데이트
    def update(self, game_screen):
        self.move(game_screen)

        # move가 순수 가상 함수이므로
        super().only_jump()