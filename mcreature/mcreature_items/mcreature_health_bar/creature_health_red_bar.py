import pygame

RED = (255, 0, 0)

class CreatureHealthRedBar:
    def __init__(self, healthbar, width, height):
        self.width = width
        self.height = height
        
        self.located(healthbar)

    def located(self, healthbar):
        self.x = healthbar.x + 11
        self.y = healthbar.y + 12.5

    def draw(self, screen):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width * 0.8, self.height])

    def update(self, healthbar):
        self.located(healthbar)