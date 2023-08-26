from mcreature.creature_manager import CreatureManager

class PlayerManager(CreatureManager):
    def __init__(self):
        super().__init__()

    def add_player(self, addCreature):
        super().add_creature(addCreature)

    def list_player(self):
        super().list_creature()

    def draw_player(self, screen):
        super().draw_creature(screen)

    def update_player(self, game_screen):
        for indexPlayer in self.creatures:
            indexPlayer.update(game_screen)