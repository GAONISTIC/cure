class CreatureManager:
    def __init__(self):
        self.creatures = []

    def add_creature(self, addCreature):
        self.creatures.append(addCreature)

    def list_creature(self):
        for indexCreature in self.creatures:
            print(indexCreature.name)

    def draw_creature(self, screen):
        for indexCreature in self.creatures:
            indexCreature.draw(screen)

    def update_creature(self):
        for indexCreature in self.creatures:
            indexCreature.update()