# 무기 공격 관련 함수
# 예를 들어, 어떤 크리쳐에게 공격하는 지 등을 나타냄

def is_robot_attacked(weapon, robot_manager):
    for creature in robot_manager.creatures:
        if is_in(weapon, creature):
            if creature.id not in weapon.save_attacked_robot:
                creature.health -= weapon.power
                weapon.save_attacked_robot.append(creature.id)

# 어떤 크리쳐가 내 범위 안에 들어왔는지 판별하는 함수
def is_in(weapon, creature):
    start_weapon_x = weapon.x
    end_weapon_x = weapon.x + weapon.width
    if creature.x >= start_weapon_x and creature.x <= end_weapon_x:
        return True
    else:
        return False