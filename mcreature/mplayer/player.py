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
        self.playerType = playerType

    def move(self, game_screen):
        keys = pygame.key.get_pressed()
        move = False
        if keys[PlayerKey.MOVE_LEFT.value]:
            cmove.move_left(self)
            move = True
            self.left_or_right = "left"

        if keys[PlayerKey.MOVE_RIGHT.value]:
            cmove.move_right(self)
            move = True
            self.left_or_right = "right"

        if keys[PlayerKey.MOVE_JUMP.value]:
            cmove.set_is_jumping(self)

        if keys[PlayerKey.MOVE_DOWN.value]:
            cmove.down(self)

        if keys[PlayerKey.ATT_B1.value]:
            pattack.B1_ATTACK()

        if keys[PlayerKey.ATT_B2.value]:
            pattack.B2_ATTACK()

        if keys[PlayerKey.ATT_CM.value]:
            pattack.CM_ATTACK()

        if keys[PlayerKey.ATT_S1.value]:
            pattack.S1_ATTACK()

        if keys[PlayerKey.ATT_S2.value]:
            pattack.S2_ATTACK()

        if keys[PlayerKey.BROKEN_WORLD.value]:
            game_screen.change_world()

        if move == False:
            cmove.sliding(self)

        self.rect.topleft = (self.x, self.y)
        pygame.display.update()

    def update(self, game_screen):
        self.move(game_screen)
        super().only_jump()