from mcreature.creature_manager import CreatureManager

class RobotManager(CreatureManager):
    def __init__(self):
        super().__init__()

    def add_robot(self, addCreature):
        super().add_creature(addCreature)

    def list_robot(self):
        super().list_creature()

    def draw_robot(self, screen):
        super().draw_creature(screen)

    def update_robot(self, p1):
        for indexRobot in self.creatures:
            indexRobot.update(p1)