# 메니저 통합 메니저

class mmnager:
    def __init__(self):
        self.managers = []

    def draw(self, screen):
        for managers in self.managers:
            managers.draw(screen)

    def update(self, parent):
        for managers in self.managers:
            managers.update(parent)