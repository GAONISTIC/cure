# 로봇 관리 클래스

from mcreature.creature_manager import CreatureManager

# 크리쳐 메니저와 하는 일이 같다
class RobotManager(CreatureManager):
    def __init__(self):
        super().__init__()

    def add_element(self, addCreature):
        super().add_element(addCreature)

    def list_element(self):
        super().list_element()

    def draw_element(self, screen):
        super().draw_element(screen)

    def update_element(self, p1):
        for indexRobot in self.creatures:
            indexRobot.update(p1)