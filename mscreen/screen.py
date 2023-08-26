# 깨어진 세계이냐 아니냐 그것이 문제로다

from mscreen.screen_set import Screen_set
import mgame_manager.settings as ms

class Screen:
    def __init__(self):
        # 현재 세계 지정
        self.world = Screen_set.NORMAL_WORLD.value

    def change_world(self):
        # 짝수면 깨어진 세계임
        self.world += 1

    def screen_fill(self, screen):
        if self.world % 2 == Screen_set.BROKEN_WORLD.value:
            screen.fill(ms.BLACK)

        elif self.world % 2 == Screen_set.NORMAL_WORLD.value:
            screen.fill(ms.WHITE)