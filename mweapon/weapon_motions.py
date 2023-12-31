# 무기 움직임 관련 함수 모음

import mgame_manager.settings as ms

def B1ATTACK_motion(current_weapon):
    if not current_weapon.is_attacking:
        current_weapon.is_attacking = True
        current_weapon.start_attack_frame = ms.frame_count
        current_weapon.x += 700

def checking_motion(current_weapon):
    if current_weapon.is_attacking and ms.frame_count - current_weapon.start_attack_frame > current_weapon.delay_attack_frame:
        current_weapon.is_attacking = False

    elif current_weapon.is_attacking:
        current_weapon.x -= 700 / current_weapon.delay_attack_frame