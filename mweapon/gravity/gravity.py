import pygame
import math
from mgame_manager.settings import *

class GravityCircle:
    def __init__(self, x, y, radius, ALPHA):
        self.x = x
        self.y = y
        self.radius = radius
        self.ALPHA = ALPHA
        
    def draw(self, screen):
        transparent_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(transparent_surface, (BLACK[0], BLACK[1], BLACK[2], self.ALPHA), (self.radius, self.radius), self.radius)

        # 중앙에 그리기 위한 좌표 계산
        blit_x = self.x - self.radius
        blit_y = self.y - self.radius

        screen.blit(transparent_surface, (blit_x, blit_y))

class GravityAttack:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
        self.beginning_G = 1
        self.ed_creatures = []
        self.creatures_ID = []
        self.creatures_G = []
        self.increasing_G = 0.1

    def increase_G(self):
        for i in range(0, len(self.creatures_G)):
            self.creatures_G[i] += self.increasing_G

    def append_creatures(self, temp_creature):
        if temp_creature.id not in self.creatures_ID:

            self.creatures_ID.append(temp_creature.id)
            self.creatures_G.append(self.beginning_G)
            self.ed_creatures.append(temp_creature)

    def move_gravity(g, self, G):
        # 중력점 g를 일차 함수로 간주하여 물체 self를 이동시킴

        g.G = G

        middle_x = self.x + self.width / 2
        middle_y = self.y + self.height / 2

        if g.x == middle_x and g.y == middle_y:
            pass
        elif g.x != middle_x:
            a = (-g.y + middle_y) / (g.x - middle_x)
            dx = g.G if middle_x <= g.x else -1 * g.G
            dy = a * dx
            if (middle_x < g.x and middle_x + dx > g.x) or (middle_x > g.x and middle_x + dx < g.x):
                middle_x = g.x
                middle_y = g.y
            else:
                middle_x += dx
                middle_y -= dy
        else:
            dy = g.G if middle_y < g.y else -1 * g.G
            if (middle_y < g.y and middle_y + dy > g.y) or (middle_y > g.y and middle_y + dy < g.y):
                middle_y = g.y
            else:
                middle_y += dy

        self.x  = middle_x - self.width / 2
        self.y = middle_y - self.height / 2

    def creatures_in_gravity(self, creature):
        min_x = creature.x
        max_x = creature.x + creature.width

        min_y = creature.y
        max_y = creature.y + creature.height

        min_rx = self.x - self.radius
        max_rx = self.x + self.radius

        min_ry = self.y - self.radius
        max_ry = self.y + self.radius

        # print(f"min: {min_x, min_y}, max: {max_x, max_y}, rmin: {min_rx, min_ry}, rmax: {max_rx, max_ry}")

        if min_x >= min_rx and max_x <= max_rx and min_y <= max_ry:
            return True
        else:
            return False

    def holding_gravity(self):
        for i in range(0, len(self.creatures_G)):
            if self.creatures_in_gravity(self.ed_creatures[i]):
                self.move_gravity(self.ed_creatures[i], self.creatures_G[i])
    
    def move(self, theta):
        # 거리
        distance = 1
        
        # 각도를 라디안으로 변환
        radians = math.radians(theta)

        # 새로운 x, y 좌표 계산
        new_x = self.x + distance * math.cos(radians)
        new_y = self.y + distance * math.sin(radians)

        # 좌표를 업데이트
        self.x = new_x
        self.y = new_y


    def draw(self, screen):
        for i in range(1, self.radius):
            GravityCircle(self.x, self.y, i, 15).draw(screen)

        self.increase_G()
        self.holding_gravity()