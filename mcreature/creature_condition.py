# 크리쳐 상태를 확인하는 함수 모음

def is_dead(creature):
    if creature.health <= 0:
        return True
    else:
        return False