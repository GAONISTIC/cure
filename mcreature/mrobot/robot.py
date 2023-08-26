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
        pygame.display.update()

    def update(self, p1):
        self.move(p1)