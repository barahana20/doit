from tkinter import *
import os
import sys
import pygame
import time
import random

class Zombie:
    def __init__(self, enemy_money, enemy_hp):
        print("Zombie 객체가 호출되었습니다")

    def normal_zombie(self):
        print("normal_zombie 객체가 호출되었습니다")
                
class Sword:
    def __init__(self, money, damage):
        self.money = money
        self.damage = damage
    # 여기서 money와 damage를 수정하는게 트루정보이다.
    def wooden_sword(self, money, damage):
        self.money = 1000
        self.damage = 10
        return (self.money, self.damage)
    def stone_sword(self, money, damage):
        self.money = 2000
        self.damage = 20
        return (self.money, self.damage)
    def iron_sword(self, money, damage):
        self.money = 4000
        self.damage = 40
        return (self.money, self.damage)
    def golden_sword(self, money, damage):
        self.money = 8000
        self.damage = 80
        return (self.money, self.damage)
    def diamond_sword(self, money, damage):
        self.money = 16000
        self.damage = 100
    def netherite_sword(self, money, damage):
        self.money = 32000
        self.damage = 300
    def attack_effect(self):
        pass
# class Return_money:
#     pass
# class Return_damage(Sword):
#     def __init__(self):
#         Sword.__init__(self, money, damage)
#         pass
#     def return_damage(self):
#         return_wooden_sword_damage = Sword(1000,4)
#         return return_wooden_sword_damage.damage

def random_appear():
    a = random.randint(0,screen_width-enemy_width)
    b = random.randint(0,screen_height-enemy_height)
    return (a,b)

# hp 바를 적 머리 위에 소환하도록 하는 함수
def hp_bar():
    pygame.draw.rect(screen, RED, ((enemy_x_pos),(enemy_y_pos-10),100,10))
    pygame.draw.rect(screen, GREEN, ((enemy_x_pos),(enemy_y_pos-10),(enemy_hp//2),10))

# 만약 wooden_sword가 활성화 상태라면 공격을 했을 때 어택 모션이 취해지도록 하는 함수
def wooden_sword_ruuning_IfTrue_attack():
    if wooden_sword_running == True:
        # print("wooden_sword_running이 True 일때 wooden_sword_running_IfTrue_attack 함수가 실행되었습니다")
        wooden_sword.fill(transparent)
        screen.blit(wooden_sword_attack, (wooden_sword_x_pos, wooden_sword_y_pos))

# 만약 stone_sword가 활성화 상태라면 공격을 했을 때 어택 모션이 취해지도록 하는 함수
def stone_sword_ruuning_IfTrue_attack():
    if stone_sword_running == True:
        # print("stone_sword_running이 True 일때 stone_sword_running_IfTrue_attack 함수가 실행되었습니다")
        stone_sword.fill(transparent)
        screen.blit(stone_sword_attack, (stone_sword_x_pos, stone_sword_y_pos)) 
# 만약 iron_sword가 활성화 상태라면 공격을 했을 때 어택 모션이 취해지도록 하는 함수          
def iron_sword_ruuning_IfTrue_attack():
    if iron_sword_running == True:
        # print("iron_sword_running이 True 일때 iron_sword_running_IfTrue_attack 함수가 실행되었습니다")
        iron_sword.fill(transparent)
        screen.blit(iron_sword_attack, (iron_sword_x_pos, iron_sword_y_pos))   
# 만약 golden_sword가 활성화 상태라면 공격을 했을 때 어택 모션이 취해지도록 하는 함수          
def golden_sword_ruuning_IfTrue_attack():
    if golden_sword_running == True:
        # print("golden_sword_running이 True 일때 golden_sword_running_IfTrue_attack 함수가 실행되었습니다")
        golden_sword.fill(transparent)
        screen.blit(golden_sword_attack, (golden_sword_x_pos, golden_sword_y_pos))   


pygame.init()

screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("검 키우기") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("resources/background.png")

# 적 enemy 캐릭터
enemy = pygame.image.load("resources/normal_zombie.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width-enemy_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)# 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)


#FPS
clock = pygame.time.Clock()

# 이동 속도
wooden_sword_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)


wooden_sword = pygame.image.load("resources/wooden_sword.png")
wooden_sword_size = wooden_sword.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_width = wooden_sword_size[0] # 캐릭터의 가로 크기
wooden_sword_height = wooden_sword_size[1] # 캐릭터의 세로 크기
wooden_sword_x_pos = (screen_width-wooden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
wooden_sword_y_pos = screen_height - wooden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

wooden_sword_attack = pygame.image.load("resources/wooden_sword_attack.png")
wooden_sword_attack_size = wooden_sword_attack.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_attack_width = wooden_sword_attack_size[0] # 캐릭터의 가로 크기
wooden_sword_attack_height = wooden_sword_attack_size[1] # 캐릭터의 세로 크기
wooden_sword_attack_x_pos = wooden_sword_x_pos
wooden_sword_attack_y_pos = wooden_sword_y_pos

stone_sword = pygame.image.load("resources/stone_sword.png")
stone_sword_size = stone_sword.get_rect().size # 이미지의 크기를 구해옴
stone_sword_width = stone_sword_size[0] # 캐릭터의 가로 크기
stone_sword_height = stone_sword_size[1] # 캐릭터의 세로 크기
stone_sword_x_pos = (screen_width-stone_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
stone_sword_y_pos = screen_height - stone_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

stone_sword_attack = pygame.image.load("resources/stone_sword_attack.png")
stone_sword_attack_size = stone_sword_attack.get_rect().size # 이미지의 크기를 구해옴
stone_sword_attack_width = stone_sword_attack_size[0] # 캐릭터의 가로 크기
stone_sword_attack_height = stone_sword_attack_size[1] # 캐릭터의 세로 크기
stone_sword_attack_x_pos = stone_sword_x_pos
stone_sword_attack_y_pos = stone_sword_y_pos

iron_sword = pygame.image.load("resources/iron_sword.png")
iron_sword_size = iron_sword.get_rect().size # 이미지의 크기를 구해옴
iron_sword_width = iron_sword_size[0] # 캐릭터의 가로 크기
iron_sword_height = iron_sword_size[1] # 캐릭터의 세로 크기
iron_sword_x_pos = (screen_width-iron_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
iron_sword_y_pos = screen_height - iron_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

iron_sword_attack = pygame.image.load("resources/iron_sword_attack.png")
iron_sword_attack_size = iron_sword_attack.get_rect().size # 이미지의 크기를 구해옴
iron_sword_attack_width = iron_sword_attack_size[0] # 캐릭터의 가로 크기
iron_sword_attack_height = iron_sword_attack_size[1] # 캐릭터의 세로 크기
iron_sword_attack_x_pos = iron_sword_x_pos
iron_sword_attack_y_pos = iron_sword_y_pos

golden_sword = pygame.image.load("resources/golden_sword.png")
golden_sword_size = golden_sword.get_rect().size # 이미지의 크기를 구해옴
golden_sword_width = golden_sword_size[0] # 캐릭터의 가로 크기
golden_sword_height = golden_sword_size[1] # 캐릭터의 세로 크기
golden_sword_x_pos = (screen_width-golden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
golden_sword_y_pos = screen_height - golden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

golden_sword_attack = pygame.image.load("resources/golden_sword_attack.png")
golden_sword_attack_size = golden_sword_attack.get_rect().size # 이미지의 크기를 구해옴
golden_sword_attack_width = golden_sword_attack_size[0] # 캐릭터의 가로 크기
golden_sword_attack_height = golden_sword_attack_size[1] # 캐릭터의 세로 크기
golden_sword_attack_x_pos = golden_sword_x_pos
golden_sword_attack_y_pos = golden_sword_y_pos

diamond_sword = pygame.image.load("resources/diamond_sword.png")
diamond_sword_size = diamond_sword.get_rect().size # 이미지의 크기를 구해옴
diamond_sword_width = diamond_sword_size[0] # 캐릭터의 가로 크기
diamond_sword_height = diamond_sword_size[1] # 캐릭터의 세로 크기
diamond_sword_x_pos = (screen_width-diamond_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
diamond_sword_y_pos = screen_height - diamond_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

diamond_sword_attack = pygame.image.load("resources/diamond_sword_attack.png")
diamond_sword_attack_size = diamond_sword_attack.get_rect().size # 이미지의 크기를 구해옴
diamond_sword_attack_width = diamond_sword_attack_size[0] # 캐릭터의 가로 크기
diamond_sword_attack_height = diamond_sword_attack_size[1] # 캐릭터의 세로 크기
diamond_sword_attack_x_pos = diamond_sword_x_pos
diamond_sword_attack_y_pos = diamond_sword_y_pos

netherite_sword = pygame.image.load("resources/netherite_sword.png")
netherite_sword_size = netherite_sword.get_rect().size # 이미지의 크기를 구해옴
netherite_sword_width = netherite_sword_size[0] # 캐릭터의 가로 크기
netherite_sword_height = netherite_sword_size[1] # 캐릭터의 세로 크기
netherite_sword_x_pos = (screen_width-netherite_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
netherite_sword_y_pos = screen_height - netherite_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

netherite_sword_attack = pygame.image.load("resources/netherite_sword_attack.png")
netherite_sword_attack_size = netherite_sword_attack.get_rect().size # 이미지의 크기를 구해옴
netherite_sword_attack_width = netherite_sword_attack_size[0] # 캐릭터의 가로 크기
netherite_sword_attack_height = netherite_sword_attack_size[1] # 캐릭터의 세로 크기
netherite_sword_attack_x_pos = netherite_sword_x_pos
netherite_sword_attack_y_pos = netherite_sword_y_pos

running = True

to_x = 0
to_y = 0
transparent = (0, 0, 0, 0)
enemy_update = False
enemy_cnt = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

global enemy_hp
enemy_hp = 200

wooden_sword1 = Sword(0,0) # 초기화
stone_sword1 = Sword(0,0) # 초기화
iron_sword1 = Sword(0,0) # 초기화
golden_sword1 = Sword(0,0) # 초기화
diamond_sword1 = Sword(0,0) # 초기화
netherite_sword1 = Sword(0,0) # 초기화

wooden_sword_running = True # 처음에는 wooden_sword만 활성화
stone_sword_running = False
iron_sword_running = False
golden_sword_running = False
diamond_sword_running = False
netherite_sword_running = False

wooden_sword_rect_running = True
stone_sword_rect_running = False
iron_sword_rect_running = False
golden_sword_rect_running = False
diamond_sword_rect_running = False
netherite_sword_rect_running = False

while running:
    dt = clock.tick(100) # 게임 화면의 초당 프레임 수를 설정
    screen.fill(BLACK)

    # hp_bar()

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 왼쪽
                to_x -= wooden_sword_speed
            elif event.key == pygame.K_RIGHT: # 오른쪽
                to_x += wooden_sword_speed
            elif event.key == pygame.K_UP: # 위쪽
                to_y -= wooden_sword_speed
            elif event.key == pygame.K_DOWN: # 아래쪽
                to_y += wooden_sword_speed
            elif event.key == pygame.K_SPACE: # 스페이스바_공격키
                # print("스페이스바를 눌렀습니다.")
                # 어떤 sword가 running 상태인지 확인하고 그 객체를 투명화 및 attack 사진을 출력함.
                wooden_sword_ruuning_IfTrue_attack()
                stone_sword_ruuning_IfTrue_attack()
                iron_sword_ruuning_IfTrue_attack()
                golden_sword_ruuning_IfTrue_attack()
                
                pygame.display.update() # 게임 화면을 다시 그리기
                
                # wooden_sword의 충돌 체크
                if wooden_sword_rect_running == True:
                    if wooden_sword_rect.colliderect(enemy_rect):
                        enemy_update = True
                        enemy_x_pos, enemy_y_pos = random_appear()
                        enemy_hp = enemy_hp - int(wooden_sword1.wooden_sword(0,0)[1]) - 20
                # stone_sword의 충돌 체크
                elif stone_sword_rect_running == True:
                    if stone_sword_rect.colliderect(enemy_rect):
                        enemy_update = True
                        enemy_x_pos, enemy_y_pos = random_appear()
                        enemy_hp = enemy_hp - int(stone_sword1.stone_sword(0,0)[1]) - 20
                elif iron_sword_rect_running == True:
                    if iron_sword_rect.colliderect(enemy_rect):
                        enemy_update = True
                        enemy_x_pos, enemy_y_pos = random_appear()
                        enemy_hp = enemy_hp - int(iron_sword1.iron_sword(0,0)[1]) - 20
                elif golden_sword_rect_running == True:
                    if golden_sword_rect.colliderect(enemy_rect):
                        enemy_update = True
                        enemy_x_pos, enemy_y_pos = random_appear()
                        enemy_hp = enemy_hp - int(golden_sword1.golden_sword(0,0)[1]) - 20
                    
                enemy_update = False  # 이걸 해야 enemy를 화면에 다시 그릴 수 있음.

                time.sleep(0.05)

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_SPACE:
                # 스페이스바를 뗐을 떄, 어떤 Sword 객체가 running 상태인지에 따라 다른 Sword 소환
                if wooden_sword_running == True:
                    wooden_sword = pygame.image.load("resources/wooden_sword.png")
                # pygame.display.update() # 게임 화면을 다시 그리기
                elif stone_sword_running == True:
                    stone_sword = pygame.image.load("resources/stone_sword.png")
                
                elif iron_sword_running == True:
                    iron_sword = pygame.image.load("resources/iron_sword.png")

                elif golden_sword_running == True:
                    golden_sword = pygame.image.load("resources/golden_sword.png")
                
                # if enemy_cnt == 1:
                #     wooden_sword.fill(transparent)
                
                # elif enemy_cnt == 2:
                #     stone_sword.fill(transparent)
    
    # 충돌 처리를 위한 rect 정보 업데이트

    # wooden_sword의 방향키에 따른 이동 속도 조절            
    wooden_sword_x_pos += to_x * dt
    wooden_sword_y_pos += to_y * dt

    # wooden_sword의 가로 경계값 처리
    if wooden_sword_x_pos < 0:
        wooden_sword_x_pos = 0
    elif wooden_sword_x_pos > screen_width - wooden_sword_width:
        wooden_sword_x_pos = screen_width - wooden_sword_width

    # wooden_sword의 세로 경계값 처리
    if wooden_sword_y_pos < 0:
        wooden_sword_y_pos = 0
    elif wooden_sword_y_pos > screen_height - wooden_sword_height:
        wooden_sword_y_pos = screen_height - wooden_sword_height
        
    wooden_sword_rect = wooden_sword.get_rect()
    wooden_sword_rect.left = wooden_sword_x_pos
    wooden_sword_rect.top = wooden_sword_y_pos

    # stone_sword의 방향키에 따른 이동 속도 조절
    stone_sword_x_pos += to_x * dt
    stone_sword_y_pos += to_y * dt

    # stone_sword의 가로 경계값 처리
    if stone_sword_x_pos < 0:
        stone_sword_x_pos = 0
    elif stone_sword_x_pos > screen_width - stone_sword_width:
        stone_sword_x_pos = screen_width - stone_sword_width

    # stone_sword의 세로 경계값 처리
    if stone_sword_y_pos < 0:
        stone_sword_y_pos = 0
    elif stone_sword_y_pos > screen_height - stone_sword_height:
        stone_sword_y_pos = screen_height - stone_sword_height

    stone_sword_rect = stone_sword.get_rect()
    stone_sword_rect.left = stone_sword_x_pos
    stone_sword_rect.top = stone_sword_y_pos

    # iron_sword의 방향키에 따른 이동 속도 조절
    iron_sword_x_pos += to_x * dt
    iron_sword_y_pos += to_y * dt

    # iron_sword의 가로 경계값 처리
    if iron_sword_x_pos < 0:
        iron_sword_x_pos = 0
    elif iron_sword_x_pos > screen_width - iron_sword_width:
        iron_sword_x_pos = screen_width - iron_sword_width

    # iron_sword의 세로 경계값 처리
    if iron_sword_y_pos < 0:
        iron_sword_y_pos = 0
    elif iron_sword_y_pos > screen_height - iron_sword_height:
        iron_sword_y_pos = screen_height - iron_sword_height

    iron_sword_rect = iron_sword.get_rect()
    iron_sword_rect.left = iron_sword_x_pos
    iron_sword_rect.top = iron_sword_y_pos

    # golden_sword의 방향키에 따른 이동 속도 조절
    golden_sword_x_pos += to_x * dt
    golden_sword_y_pos += to_y * dt

    # golden_sword의 가로 경계값 처리
    if golden_sword_x_pos < 0:
        golden_sword_x_pos = 0
    elif golden_sword_x_pos > screen_width - golden_sword_width:
        golden_sword_x_pos = screen_width - golden_sword_width

    # golden_sword의 세로 경계값 처리
    if golden_sword_y_pos < 0:
        golden_sword_y_pos = 0
    elif golden_sword_y_pos > screen_height - golden_sword_height:
        golden_sword_y_pos = screen_height - golden_sword_height

    golden_sword_rect = golden_sword.get_rect()
    golden_sword_rect.left = golden_sword_x_pos
    golden_sword_rect.top = golden_sword_y_pos

    # 충돌 처리를 위한 enemy의 rect 정보 업데이트
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
        
    screen.blit(background,(0,0)) # 배경 그리기
    
    # 적 체력이 0 이하이면 체력이 다시 200으로 회복
    if enemy_hp <= 0:
        enemy_hp = 200
        enemy_cnt += 1
        enemy_update == False
    
    # enemy_update가 False 일 때 enemy를 화면에 다시 그리기
    if enemy_update == False:
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    if enemy_cnt == 1:
        wooden_sword.fill(transparent)
        wooden_sword_running, wooden_sword_rect_running = False, False
        stone_sword_running, stone_sword_rect_running = True, True
        
    elif enemy_cnt == 2:
        stone_sword.fill(transparent)
        stone_sword_running, stone_sword_rect_running = False, False
        iron_sword_running, iron_sword_rect_running = True, True
    
    elif enemy_cnt == 3:
        iron_sword.fill(transparent)
        iron_sword_running, iron_sword_rect_running = False, False
        golden_sword_running, golden_sword_rect_running = True, True
    

    hp_bar() # hp 바 생성
    
    # 어떤 sword 객체가 나올지 결정
    if wooden_sword_running == True:
        screen.blit(wooden_sword, (wooden_sword_x_pos, wooden_sword_y_pos))

    elif stone_sword_running == True:
        screen.blit(stone_sword, (stone_sword_x_pos, stone_sword_y_pos))
    
    elif iron_sword_running == True:
        screen.blit(iron_sword, (iron_sword_x_pos, iron_sword_y_pos))   
    
    elif golden_sword_running == True:
        screen.blit(golden_sword, (golden_sword_x_pos, golden_sword_y_pos))   

    kill_enemy_cnt = "kill : " + str(enemy_cnt)
    # 게임 오버 메시지
    msg = game_font.render(kill_enemy_cnt, True, RED) # 빨간색
    msg_rect = msg.get_rect(center=(40,20))
    screen.blit(msg, msg_rect)

    pygame.display.update() # 게임 화면을 다시 그리기

pygame.quit()