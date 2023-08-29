# 로봇 클래스

from mcreature.creature import Creature
import assets.functions as af
import pygame

class Robot(Creature):
    def __init__(self, name, health, power, defense, speed, width, height, x, y, jumpSize):
        filepath = af.find_robot_image_directory("basic", "gravity")
        super().__init__(name, health, power, defense, speed, width, height, x, y, jumpSize, filepath)

    def move(self, p1):
        self.x = p1.x + 500
        self.y = p1.y

        self.rect.topleft = (self.x, self.y)

    # 로봇 업데이트
    def update(self, p1):
        self.move(p1)
        # 점프는 굳이 확인할 필요가 없다
        super().check_condition()