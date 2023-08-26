from mgame_manager.settings import *

def move_left(current_creature):
    current_creature.speed = current_creature.max_speed
    if current_creature.x - current_creature.speed < 0:
        current_creature.x = 0
    else:
        current_creature.x -= current_creature.speed

def move_right(current_creature):
    current_creature.speed = current_creature.max_speed
    if current_creature.x + current_creature.speed > screen_width - current_creature.width:
        current_creature.x = screen_width - current_creature.width
    else:
        current_creature.x += current_creature.speed

def sliding(current_creature):
    if current_creature.speed <= 0:
        current_creature.speed = 0
        return
    else:
        current_creature.speed -= current_creature.sliding_speed
    if current_creature.left_or_right == "left":
        if current_creature.x - current_creature.speed < 0:
            current_creature.speed = 0
            current_creature.x = 0
        else:
            current_creature.x -= current_creature.speed

    elif current_creature.left_or_right == "right":
        if current_creature.x + current_creature.speed > screen_width - current_creature.width:
            current_creature.speed = 0
            current_creature.x = screen_width - current_creature.width
        else:
            current_creature.x += current_creature.speed

def set_is_jumping(current_creature):
    # isJumping == False: isJumping = True
    # isJumping == True: X
    if current_creature.isJumping == False:
        current_creature.isJumping = True
        current_creature.nowy = current_creature.y
        current_creature.jumpingOrNot = -1

def jump(current_creature):
    # isJumping == True일때만 실행
    if current_creature.isJumping:
        # 현재 y좌표 저장
        # 점프전 y좌표 + jumpsize > y
        current_creature.y += current_creature.jumpSize * current_creature.jumpingOrNot * current_creature.jumpK / 10
        if current_creature.nowy - current_creature.jumpSize > current_creature.y:
            current_creature.jumpingOrNot = 1
            # 떨어질 때는 느리게
            current_creature.jumpK = 0.5

        if current_creature.y > current_creature.nowy:
            current_creature.y = current_creature.nowy
            current_creature.isJumping = False
            current_creature.jumpK = 1.1

def down(current_creature):
    print("DOWN")