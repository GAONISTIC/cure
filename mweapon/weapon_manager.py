class WeaponManager:
    def __init__(self):
        self.weapons = []

    def add_weapon(self, addWeapon):
        self.weapons.append(addWeapon)

    def list_weapon(self):
        for indexWeapon in self.weapons:
            print(indexWeapon.name)

    def draw_weapon(self, screen):
        for indexWeapon in self.weapons:
            indexWeapon.draw(screen)

    def update_weapon(self, parent_player):
        for indexWeapon in self.weapons:
            indexWeapon.update(parent_player)