# 플레이어 관리 클래스

from mcreature.creature_manager import CreatureManager

# 플레이어 메니저는 크리쳐 메니저와 하는 일이 같다
class PlayerManager(CreatureManager):
    def __init__(self):
        super().__init__()

    def add_element(self, addCreature):
        super().add_element(addCreature)

    def list_element(self):
        super().list_element()

    def draw_element(self, screen):
        super().draw_element(screen)

    def update_element(self, game_screen):
        for indexPlayer in self.creatures:
            # game_screen을 넣는 이유: 깨어진 세계 이동을 짜야 하기 때문
            indexPlayer.update(game_screen)