# 크리쳐 관리 클래스

class CreatureManager:
    def __init__(self):
        # 크리쳐 배열 생성
        self.creatures = []

    def add_element(self, addCreature):
        # 크리쳐 추가
        self.creatures.append(addCreature)

    def list_element(self):
        # 크리쳐 확인
        for indexCreature in self.creatures:
            print(indexCreature.name)

    def draw_element(self, screen):
        # 크리쳐 그리기
        for indexCreature in self.creatures:
            indexCreature.draw(screen)

    def update_element(self):
        # 크리쳐 업데이트
        for indexCreature in self.creatures:
            indexCreature.update()