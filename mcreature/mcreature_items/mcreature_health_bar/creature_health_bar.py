import pygame
from mcreature.mcreature_items.mcreature_health_bar.creature_health_red_bar import CreatureHealthRedBar

class CreatureHealthBar:
    def __init__(self, mother_creature, width, height):
        self.mother_creature = mother_creature
        self.max_health = self.mother_creature.health
        self.now_health = self.mother_creature.health
        self.set_percent_health()
        self.x = self.mother_creature.x
        self.y = self.mother_creature.y - self.mother_creature.height / 3
        self.width = width
        self.height = height

        self.filepath = "C:/Users/freeg/Desktop/cure/assets/health_bar.png"

        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.red_bar = CreatureHealthRedBar(self, 100, 15)

    def set_percent_health(self):
        self.percent_health = (self.now_health / self.max_health) * 100

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        self.red_bar.draw(screen)

    def update(self):
        self.x = self.mother_creature.x
        self.y = self.mother_creature.y - self.mother_creature.height / 3
        self.rect.topleft = (self.x, self.y)

        self.set_percent_health()

        self.red_bar.width = self.percent_health
        self.red_bar.update(self)