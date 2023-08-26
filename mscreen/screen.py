from mscreen.screen_set import Screen_set
import mgame_manager.settings as ms

class Screen:
    def __init__(self):
        self.world = Screen_set.NORMAL_WORLD.value

    def change_world(self):
        self.world += 1

    def screen_fill(self, screen):
        if self.world % 2 == Screen_set.BROKEN_WORLD.value:
            screen.fill(ms.BLACK)

        elif self.world % 2 == Screen_set.NORMAL_WORLD.value:
            screen.fill(ms.WHITE)