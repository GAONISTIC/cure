import pygame
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

        if g.x == self.x and g.y == self.y:
            pass
        elif g.x != self.x:
            a = (-g.y + self.y) / (g.x - self.x)
            dx = g.G if self.x <= g.x else -1 * g.G
            dy = a * dx
            if (self.x < g.x and self.x + dx > g.x) or (self.x > g.x and self.x + dx < g.x):
                self.x = g.x
                self.y = g.y
            else:
                self.x += dx
                self.y -= dy
        else:
            dy = g.G if self.y < g.y else -1 * g.G
            if (self.y < g.y and self.y + dy > g.y) or (self.y > g.y and self.y + dy < g.y):
                self.y = g.y
            else:
                self.y += dy

    def holding_gravity(self):
        for i in range(0, len(self.creatures_G)):
            self.move_gravity(self.ed_creatures[i], self.creatures_G[i])
    
    def draw(self, screen):
        GravityCircle(self.x, self.y, self.radius / 1, 128).draw(screen)
        GravityCircle(self.x, self.y, self.radius / 2, 128).draw(screen)
        GravityCircle(self.x, self.y, self.radius / 5, 128).draw(screen)

        self.increase_G()
        self.holding_gravity()