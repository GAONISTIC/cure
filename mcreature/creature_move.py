# 크리쳐 움직임 관련 함수 모음

# 스크린 크기 불러오기
from mgame_manager.settings import *

# 왼쪽으로 가는 움직임
def move_left(current_creature):
    # 슬라이딩으로 줄어든 스피드 초기화
    current_creature.speed = current_creature.max_speed

    # 맵을 넘어가는 것을 방지
    if current_creature.x - current_creature.speed < 0:
        current_creature.x = 0
    else:
        current_creature.x -= current_creature.speed

# 오른쪽으로 가는 움직임
def move_right(current_creature):
    # 슬라이딩으로 줄어든 스피드 초기화
    current_creature.speed = current_creature.max_speed

    # 맵을 넘어가는 것을 방지
    if current_creature.x + current_creature.speed > screen_width - current_creature.width:
        current_creature.x = screen_width - current_creature.width
    else:
        current_creature.x += current_creature.speed

# 슬라이딩 (관성으로 조금 앞으로 더 가는 것을 의미함)
# 슬라이딩 매커니즘:
# 1. 움직임이 멈추면 실행
# 2. 마지막에 왼쪽으로 갔다면 왼쪽, 오른쪽으로 갔다면 오른쪽으로 감
# 3. 그 방향으로 점점 스피드를 줄이며 x좌표 이동
# 4. 만약 줄어든 스피드가 0 이하이면 스피드를 0으로 만들고 함수 실행 종료

def sliding(current_creature):
    # 슬라이딩할 때 뒤로 가는 것을 방지
    if current_creature.speed <= 0:
        current_creature.speed = 0
        # 쓸데없는 계산 줄이기
        return
    else:
        # 스피드 줄이기
        current_creature.speed -= current_creature.sliding_speed

    # 왼쪽
    if current_creature.left_or_right == "left":
        # 밖으로 나가는 것을 방지
        if current_creature.x - current_creature.speed < 0:
            # 맵보다 더 슬라이딩 할 필요 없으므로 슬라이딩 종료
            current_creature.speed = 0
            current_creature.x = 0
        
        # 슬라이딩 하기
        else:
            current_creature.x -= current_creature.speed
    
    # 오른쪽
    elif current_creature.left_or_right == "right":
        # 맵 밖으로 나가는 것을 방지
        if current_creature.x + current_creature.speed > screen_width - current_creature.width:
            # 맵보다 더 슬라이딩 할 필요 없으므로 종료
            current_creature.speed = 0
            current_creature.x = screen_width - current_creature.width
        
        # 슬라이딩 하기
        else:
            current_creature.x += current_creature.speed

# 점프하는지 안하는지 확인하는 함수
# 이 함수는 점프 키를 눌렀을 때만 실행됨
def set_is_jumping(current_creature):
    # 점프를 하지 않았다면
    if current_creature.isJumping == False:
        # 점프하는 상태로 바꾸기(이중 점프 방지)
        current_creature.isJumping = True

        # 바닥의 y좌표 기록
        current_creature.nowy = current_creature.y

        # 위로 뜨기
        current_creature.jumpingOrNot = -1

# 점프 함수
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