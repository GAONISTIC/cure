# 무기 관리 클래스

# 메니저 클래스는 대부분 역할이 같다
class WeaponManager:
    def __init__(self):
        self.weapons = []

    def add_element(self, addWeapon):
        self.weapons.append(addWeapon)

    def list_element(self):
        for indexWeapon in self.weapons:
            print(indexWeapon.name)

    def draw_element(self, screen):
        for indexWeapon in self.weapons:
            indexWeapon.draw(screen)

    def update_element(self, parent_player):
        for indexWeapon in self.weapons:
            indexWeapon.update(parent_player)