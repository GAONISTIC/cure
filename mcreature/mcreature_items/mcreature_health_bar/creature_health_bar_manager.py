class CreatureHealthBarManager:
    def __init__(self):
        self.healthBars = []

    def add_healthBar(self, addhealthBar):
        self.healthBars.append(addhealthBar)

    def list_healthBar(self):
        for indexhealthBar in self.healthBars:
            print(indexhealthBar.name)

    def draw_healthBar(self, screen):
        for indexhealthBar in self.healthBars:
            indexhealthBar.draw(screen)

    def update_healthBar(self):
        for indexhealthBar in self.healthBars:
            indexhealthBar.update()