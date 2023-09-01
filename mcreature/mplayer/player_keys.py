# 플레이어 조작 키 모음 열거형

from enum import Enum
import pygame

class PlayerKey(Enum):
    MOVE_LEFT = pygame.K_a
    MOVE_RIGHT = pygame.K_d
    MOVE_JUMP = pygame.K_w
    MOVE_DOWN = pygame.K_s

    ATT_B1 = pygame.K_o
    ATT_B2 = pygame.K_p
    ATT_CM = pygame.K_SPACE
    ATT_S1 = pygame.K_k
    ATT_S2 = pygame.K_l

    GRV_UP = pygame.K_UP
    GRV_DW = pygame.K_DOWN

    BROKEN_WORLD = pygame.K_SEMICOLON