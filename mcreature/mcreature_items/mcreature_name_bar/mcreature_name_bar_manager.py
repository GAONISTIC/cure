# 크리쳐 이름표 관리 클래스

class CreatureNameBarManager:
    def __init__(self):
        # 크리쳐 배열 생성
        self.nameBars = []

    def add_element(self, addnameBar):
        # 크리쳐 추가
        self.nameBars.append(addnameBar)

    def list_element(self):
        # 각각의 크리쳐 확인
        for indexNameBar in self.nameBars:
            print(indexNameBar.name)

    def draw_element(self, screen):
        # 각각의 크리쳐 그리기
        for indexNameBar in self.nameBars:
            indexNameBar.draw(screen)

    def update_element(self):
        # 각각의 크리쳐 업데이트
        for indexNameBar in self.nameBars:
            indexNameBar.update()