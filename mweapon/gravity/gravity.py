import pygame
import math
import mgame_manager.settings as ms

class GravityCircle:
    def __init__(self, x, y, radius, ALPHA):
        self.x = x
        self.y = y
        self.radius = radius
        self.ALPHA = ALPHA
        
    def draw(self, screen):
        transparent_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(transparent_surface, (ms.BLACK[0], ms.BLACK[1], ms.BLACK[2], self.ALPHA), (self.radius, self.radius), self.radius)

        # 중앙에 그리기 위한 좌표 계산
        blit_x = self.x - self.radius
        blit_y = self.y - self.radius

        screen.blit(transparent_surface, (blit_x, blit_y))

class GravityAttack:
    def __init__(self, x, y, radius, mother_creature):
        self.x = x
        self.y = y
        self.radius = radius
        
        self.beginning_G = 1
        self.ed_creatures = []
        self.creatures_ID = []
        self.creatures_G = []
        self.increasing_G = 0.1

        self.mother_creature = mother_creature

        self.R = math.sqrt(pow(self.x - self.mother_creature.x + self.mother_creature.width / 2, 2) + pow(self.y - self.mother_creature.y + self.mother_creature.height / 2, 2))

        self.is_shooting = False
        self.max_distance = 500
        self.per_distance = 50
        self.gap_distance = -1

        self.stop = False
        self.start_stop_frame = -1972
        self.gap_stop_frame = 120

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
        if self.stop or self.is_shooting:
            return
        p = self.mother_creature.x + self.mother_creature.width / 2
        q = self.mother_creature.y + self.mother_creature.height / 2

        r = self.x
        s = self.y

        # 원의 방정식: (x - p)^2 + (y - q)^2 = (r - p)^2 + (s - q)^2
        # 저 방정식에 (t, u) 점이 있음

        radius = math.sqrt(pow(r - p, 2) + pow(s - q, 2))

        dx = r - p
        dy = s - q

        radian = math.atan2(dy, dx)  # 아크탄젠트 계산
        degree = math.degrees(radian)  # 라디안 값을 각도로 변환

        # 각도에 theta를 더하고 다시 라디안으로 변환
        radian = math.radians(degree + theta)

        # 원의 방정식을 사용하여 새로운 (dx, dy) 좌표 계산
        dy = math.sin(radian) * radius + q
        dx = math.cos(radian) * radius + p

        self.x = dx
        self.y = dy

    def keep_distance(self):
        if self.is_shooting:
            return
        p = self.mother_creature.x + self.mother_creature.width / 2
        q = self.mother_creature.y + self.mother_creature.height / 2

        r = self.x
        s = self.y

        radius = int(self.R / 2 if self.is_shooting else self.R / 2)

        dx = r - p
        dy = s - q

        radian = math.atan2(dy, dx)  # 아크탄젠트 계산
        degree = math.degrees(radian)  # 라디안 값을 각도로 변환

        # 각도에 theta를 더하고 다시 라디안으로 변환
        radian = math.radians(degree)
        print(radian)

        dx = math.cos(radian) * radius + p
        dy = math.sin(radian) * radius + q

        self.x = dx
        self.y = dy

    def move_forward(self, move_value):
        move_value = move_value

        middle_x = self.mother_creature.x + self.mother_creature.width / 2
        middle_y = self.mother_creature.y + self.mother_creature.height / 2

        a = (-self.y + middle_y) / (self.x - middle_x)
        
        print(a)
        
        dx = move_value if self.x >= middle_x else -1 * move_value
        dy = a * dx

        const_x = self.x
        const_y = self.y

        self.x += dx
        self.y -= dy

        if self.check_out_of_range():
            self.x = const_x
            self.y = const_y

    def begin_shooting(self):
        if self.is_shooting == True:
            return
        self.is_shooting = True

        self.gap_distance = self.per_distance

    def checking_shooting(self):
        if self.gap_distance == 0:
            self.start_stop_frame = ms.frame_count
        
        if self.gap_distance < 0:
            self.is_shooting = False
            return
        self.move_forward(self.max_distance / self.per_distance)
        self.gap_distance -= 1

    def checking_stop(self):
        if ms.frame_count - self.start_stop_frame <= self.gap_stop_frame:
            self.stop = True
        else:
            self.stop = False
            self.move_end = False

    def check_out_of_range(self):
        if self.x < 0 or self.x >= ms.screen.get_width() or self.y < 0 or self.y >= ms.screen.get_height():
            return True
        return False

    def draw(self, screen):
        ALPHA = 10 if self.is_shooting else 3
        self.radius = int(self.R / 2 if self.is_shooting else self.R / 4)
        for i in range(1, self.radius):
            GravityCircle(self.x, self.y, i, ALPHA).draw(screen)
        
        self.increase_G()
        self.holding_gravity()

        if not self.stop:
            if not self.is_shooting:
                self.keep_distance()

            self.checking_shooting()

        self.checking_stop()