import pygame
from random import *

###############################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임") # 게임 이름

#FPS
clock = pygame.time.Clock()
###############################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("C:/doit/pygame_basic/background.png")
# background_rect = background.get_rect().size
# background_width = background_rect[0]
# background_height = background_rect[1]



character = pygame.image.load("C:/doit/pygame_basic/ningen.png")
character_rect = character.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_x_pos = (screen_width-character_width)/2
character_y_pos = screen_height-character_height

enemy = pygame.image.load("C:/doit/pygame_basic/ddong.png")
enemy_rect = enemy.get_rect().size
enemy_width = enemy_rect[0]
enemy_height = enemy_rect[1]
enemy_x_pos = randint(0,411)
enemy_y_pos = 0

print(character_width)
print(character_height)

# 이동할 좌표
to_x = 0

# 스피드 정의
character_speed = 1
enemy_speed = 3

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

level_value = 1
level_value_cnt = 0
enemy_cnt = 0


running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
             running = False # 게임이 진행중이 아님

        # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    character_x_pos += to_x * dt
    # 6. 적을 아래로 내려오게 하기
    collision_sence = True
    
    enemy_y_pos += enemy_speed

    # character 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    # enemy 세로 경계값 처리 + 새로 시작
    if enemy_y_pos > screen_height-enemy_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(1,411)
        enemy_cnt += 1

    # enemy_cnt 가 5개가 될 떄마다 1레벨 업
    if enemy_cnt == 5:
        level_value_cnt += 1
        level_value += 1
        enemy_cnt = 0

    # level_value가 1레벨 업 할때마다 속도 2 증가
    if level_value_cnt == 1:
        enemy_speed += 0.5
        level_value_cnt = 1

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    
    # 7. 레벨 출력
    level_print = str(level_value) + "level"
    level = game_font.render(level_print, True, (255,255,255))

    screen.blit(level, (10,10))
    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료
pygame.quit()