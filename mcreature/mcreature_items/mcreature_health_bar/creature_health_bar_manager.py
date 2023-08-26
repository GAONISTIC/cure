# 크리쳐의 체력바를 관리하기 위한 클래스

class CreatureHealthBarManager:
    def __init__(self):
        # 체력바 배열 생성
        self.healthBars = []

    def add_element(self, addhealthBar):
        # 체력바 추가
        self.healthBars.append(addhealthBar)

    def list_element(self):
        # 체력바 확인
        for indexhealthBar in self.healthBars:
            print(indexhealthBar.name)

    def draw_element(self, screen):
        # 체력바 그리기
        for indexhealthBar in self.healthBars:
            indexhealthBar.draw(screen)

    def update_element(self):
        # 체력바 업데이트
        for indexhealthBar in self.healthBars:
            indexhealthBar.update()