# -*- coding: utf-8 -*- 
import os
import sys
import pygame
import time
import random
from tkinter import *

class Enemy: 
    def __init__(self):
        pass
    # hp 바를 적 머리 위에 소환하도록 하는 함수
    def hp_bar(self):
        global enemy_hp
        pygame.draw.rect(screen, RED, ((enemy_x_pos),(enemy_y_pos-10),100,10))
        pygame.draw.rect(screen, GREEN, ((enemy_x_pos),(enemy_y_pos-10),(enemy_hp//2),10))
        
class Zombie(Enemy):
    def __init__(self, enemy_money, enemy_hp):
        print("Zombie 객체가 호출되었습니다")

    def normal_zombie(self):
        print("normal_zombie 객체가 호출되었습니다")
                
class Sword:
    def __init__(self, money, damage, x_pos, y_pos):
        self.money = money
        self.damage = damage
        self.x_pos = x_pos
        self.y_pos = y_pos
    # 여기서 money와 damage를 수정하는게 트루정보이다.
    def sword_generate(self, sword, money):
        sword = pygame.image.load("resources/{0}.png".format(sword))
        sword_size = sword.get_rect().size # 이미지의 크기를 구해옴
        sword_width = sword_size[0] # 캐릭터의 가로 크기
        sword_height = sword_size[1] # 캐릭터의 세로 크기
        self.x_pos = (screen_width - sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
        self.y_pos = screen_height - sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
        return (sword_width, sword_height, self.x_pos, self.y_pos, sword, money)
        # [0]:가로, [1]: 세로 [2]:x좌표 [3]:y좌표 [4]:검 사진값 반환 [5]:돈

    def sword_attack_generate(self, sword_attack, damage):
        sword_attack = pygame.image.load("resources/{0}.png".format(sword_attack))
        sword_attack_size = sword_attack.get_rect().size # 이미지의 크기를 구해옴
        sword_attack_width = sword_attack_size[0] # 캐릭터의 가로 크기
        sword_attack_height = sword_attack_size[1] # 캐릭터의 세로 크기
        sword_attack_x_pos = self.x_pos
        sword_attack_y_pos = self.y_pos
        return (sword_attack_width, sword_attack_height, sword_attack_x_pos, sword_attack_y_pos, \
                    sword_attack, damage)
        # [0]:가로, [1]:세로, [2]:x좌표 [3]:y좌표 [4]:sword_attack 사진값 반환 [5]:데미지

# class Return_money:
#     pass
# class Return_damage(Sword):
#     def __init__(self):
#         Sword.__init__(self, money, damage)
#         pass
#     def return_damage(self):
#         return_wooden_sword_damage = Sword(1000,4)
#         return return_wooden_sword_damage.damage

# 적의 위치를 랜덤으로 지정
def random_appear():
    a = random.randint(0,screen_width-enemy_width)
    b = random.randint(0,screen_height-enemy_height)
    return (a,b)

# 스페이스바를 떼었을 때 발동하는 함수
def detach_spacebar(sword_attack_running_dic):
    global sword_attack_dic
    for sword_name in sword_attack_list: # sword_attack 리스트에서 sword_name을 받아와
        if sword_attack_running_dic.get(sword_name) == True: # 그에 상응하는 sword_attack_running 값이 True이면
            sword_attack_dic.get(sword_name)[4] = pygame.image.load("resources/{0}.png".format(sword_name))
            # sword_name의 사진값을 attack 하는 사진값으로 변경한다

# 만약 sword가 활성화 상태라면 공격을 했을 때 어택 모션이 취해지도록 하는 함수
def sword_running_IfTrue_attack():
    for sword_attack_name, sword_name in zip(sword_attack_list, sword_list):
        if sword_attack_running_dic.get(sword_attack_name) == True:
            sword_attack_dic.get(sword_attack_name)[4].fill(transparent)
            screen.blit(sword_attack_dic.get(sword_attack_name)[4], (sword_x_pos, sword_y_pos)) 
# 충돌 체크 함수
def check_collision():
    global enemy_hp
    global enemy_update
    global enemy_x_pos
    global enemy_y_pos
    for sword_attack_running_rect_bool, sword_attack_rect, sword_attack_name \
                in zip(sword_attack_rect_running_dic, sword_attack_rect_dic, sword_attack_list):
        if sword_attack_rect_running_dic.get(sword_attack_running_rect_bool) == True:
            if sword_attack_rect_dic.get(sword_attack_rect).colliderect(enemy_rect):
                enemy_update = True
                # enemy_x_pos, enemy_y_pos = random_appear()
                enemy_hp -= int(sword_attack_dic.get(sword_attack_name)[5])
    
# 어떤 sword 객체가 나올지 결정하는 함수
def determine_sword_object():
    for sword_name, sword_attack_name in zip(sword_list ,sword_attack_list):
        if sword_attack_running_dic.get(sword_attack_name) == True:
            screen.blit(sword_dic.get(sword_name)[4], (sword_x_pos, sword_y_pos))

def enemy_cnt_running_onoff(enemy_cnt):
    if enemy_cnt == 1:
        sword_attack_dic.get(WOODEN_SWORD_ATTACK)[4].fill(transparent)
        sword_attack_running_dic[WOODEN_SWORD_ATTACK], sword_attack_rect_running_dic[WOODEN_SWORD_ATTACK_RUNNING_RECT] = False, False
        sword_attack_running_dic[STONE_SWORD_ATTACK], sword_attack_rect_running_dic[STONE_SWORD_ATTACK_RUNNING_RECT] = True, True

    elif enemy_cnt == 2:
        sword_attack_dic.get(STONE_SWORD_ATTACK)[4].fill(transparent)
        sword_attack_running_dic[STONE_SWORD_ATTACK], sword_attack_rect_running_dic[STONE_SWORD_ATTACK_RUNNING_RECT] = False, False
        sword_attack_running_dic[IRON_SWORD_ATTACK], sword_attack_rect_running_dic[IRON_SWORD_ATTACK_RUNNING_RECT] = True, True
        # stone_sword_running, sword_attack_rect_running_dic.get(STONE_SWORD_ATTACK_RUNNING_RECT) = False, False
        # iron_sword_running, sword_attack_rect_running_dic.get(IRON_SWORD_ATTACK_RUNNING_RECT) = True, True
    
    elif enemy_cnt == 3:
        sword_attack_dic.get(IRON_SWORD_ATTACK)[4].fill(transparent)
        sword_attack_running_dic[IRON_SWORD_ATTACK], sword_attack_rect_running_dic[IRON_SWORD_ATTACK_RUNNING_RECT] = False, False
        sword_attack_running_dic[GOLDEN_SWORD_ATTACK], sword_attack_rect_running_dic[GOLDEN_SWORD_ATTACK_RUNNING_RECT] = True, True

    elif enemy_cnt == 4:
        sword_attack_dic.get(GOLDEN_SWORD_ATTACK)[4].fill(transparent)
        sword_attack_running_dic[GOLDEN_SWORD_ATTACK], sword_attack_rect_running_dic[GOLDEN_SWORD_ATTACK_RUNNING_RECT] = False, False
        sword_attack_running_dic[DIAMOND_SWORD_ATTACK], sword_attack_rect_running_dic[DIAMOND_SWORD_ATTACK_RUNNING_RECT] = True, True
    
    elif enemy_cnt == 5:
        sword_attack_dic.get(DIAMOND_SWORD_ATTACK)[4].fill(transparent)
        sword_attack_running_dic[DIAMOND_SWORD_ATTACK], sword_attack_rect_running_dic[DIAMOND_SWORD_ATTACK_RUNNING_RECT] = False, False
        sword_attack_running_dic[NETHERITE_SWORD_ATTACK], sword_attack_rect_running_dic[NETHERITE_SWORD_ATTACK_RUNNING_RECT] = True, True

def print_msg(cnt,width, height, color):
    msg = game_font.render(cnt, True, color) # 빨간색
    msg_rect = msg.get_rect(center=(width,height))
    
    screen.blit(msg, msg_rect)


def pause_msg(PAUSE, color):
    msg = pause_font.render(PAUSE, True, color) # 검은색
    width = (screen_width // 2)
    height = (screen_height // 2)
    msg_rect = msg.get_rect(center=(width,height))
    screen.blit(msg, msg_rect)
    pygame.display.update()


def btn1_command():
    print("dd")

def inventory():
   root = Tk()
   root.title("INVENTORY")
   # root.geometry("640x480") # 가로 x 세로 지정
   root.geometry("320x480") # 가로 x 세로 + x좌표 + y좌표
   root.resizable(True, False) # x(너비), y(너비) 값 변경 불가 ( 창 크기 변경 불가 )

   label1 = Label(root, text="안녕하세요")
   label1.pack(side='left')


   btn1 = Button(root, padx=10, pady=5, text="버튼3", command=btn1_command) # 버튼 크기 유동성
   btn1.pack(side='right')


   root.mainloop()


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
pause_font = pygame.font.Font(None, 100)

running = True

to_x = 0
to_y = 0
transparent = (0, 0, 0, 0)
enemy_update = False
enemy_cnt = 0
enemy_money = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

enemy_hp = 200
original_enemy_hp = enemy_hp
enemy1 =Enemy()

total_sword = Sword(0,0,0,0)

# 검 이름 일일이 입력하기 귀찮으니까 만듦
WOODEN_SWORD = 'wooden_sword'
STONE_SWORD = 'stone_sword'
IRON_SWORD = 'iron_sword'
GOLDEN_SWORD = 'golden_sword'
DIAMOND_SWORD = 'diamond_sword'
NETHERITE_SWORD = 'netherite_sword'

WOODEN_SWORD_ATTACK = 'wooden_sword_attack'
STONE_SWORD_ATTACK = 'stone_sword_attack'
IRON_SWORD_ATTACK = 'iron_sword_attack'
GOLDEN_SWORD_ATTACK = 'golden_sword_attack'
DIAMOND_SWORD_ATTACK = 'diamond_sword_attack'
NETHERITE_SWORD_ATTACK = 'netherite_sword_attack'

WOODEN_SWORD_ATTACK_RECT = 'wooden_sword_attack_rect'
STONE_SWORD_ATTACK_RECT = 'stone_sword_attack_rect'
IRON_SWORD_ATTACK_RECT = 'iron_sword_attack_rect'
GOLDEN_SWORD_ATTACK_RECT = 'golden_sword_attack_rect'
DIAMOND_SWORD_ATTACK_RECT = 'diamond_sword_attack_rect'
NETHERITE_SWORD_ATTACK_RECT = 'netherite_sword_attack_rect'

WOODEN_SWORD_ATTACK_RUNNING_RECT = 'wooden_sword_attack_running_rect'
STONE_SWORD_ATTACK_RUNNING_RECT = 'stone_sword_attack_running_rect'
IRON_SWORD_ATTACK_RUNNING_RECT = 'iron_sword_attack_running_rect'
GOLDEN_SWORD_ATTACK_RUNNING_RECT = 'golden_sword_attack_running_rect'
DIAMOND_SWORD_ATTACK_RUNNING_RECT = 'diamond_sword_attack_running_rect'
NETHERITE_SWORD_ATTACK_RUNNING_RECT = 'netherite_sword_attack_running_rect'



WOODEN_SWORD_ATTACK_DAMAGE = 20
STONE_SWORD_ATTACK_DAMAGE = 30
IRON_SWORD_ATTACK_DAMAGE = 50
GOLDEN_SWORD_ATTACK_DAMAGE = 70
DIAMOND_SWORD_ATTACK_DAMAGE = 90
NETHERITE_SWORD_ATTACK_DAMAGE = 110

WOODEN_SWORD_MONEY = 1000
STONE_SWORD_MONEY = 2000
IRON_SWORD_MONEY = 4000
GOLDEN_SWORD_MONEY = 8000
DIAMOND_SWORD_MONEY = 16000
NETHERITE_SWORD_MONEY = 20000

sword_dic = {WOODEN_SWORD:list(total_sword.sword_generate(WOODEN_SWORD,WOODEN_SWORD_MONEY)), \
             STONE_SWORD:list(total_sword.sword_generate(STONE_SWORD,STONE_SWORD_MONEY)), \
             IRON_SWORD:list(total_sword.sword_generate(IRON_SWORD,IRON_SWORD_MONEY)), \
             GOLDEN_SWORD:list(total_sword.sword_generate(GOLDEN_SWORD,GOLDEN_SWORD_MONEY)), \
             DIAMOND_SWORD:list(total_sword.sword_generate(DIAMOND_SWORD,DIAMOND_SWORD_MONEY)), \
             NETHERITE_SWORD:list(total_sword.sword_generate(NETHERITE_SWORD,NETHERITE_SWORD_MONEY))
            }

sword_attack_dic = { WOODEN_SWORD_ATTACK:list(total_sword.sword_attack_generate(WOODEN_SWORD_ATTACK,WOODEN_SWORD_ATTACK_DAMAGE)), \
                     STONE_SWORD_ATTACK:list(total_sword.sword_attack_generate(STONE_SWORD_ATTACK, STONE_SWORD_ATTACK_DAMAGE)), \
                     IRON_SWORD_ATTACK:list(total_sword.sword_attack_generate(IRON_SWORD_ATTACK, IRON_SWORD_ATTACK_DAMAGE)), \
                     GOLDEN_SWORD_ATTACK:list(total_sword.sword_attack_generate(GOLDEN_SWORD_ATTACK, GOLDEN_SWORD_ATTACK_DAMAGE)), \
                     DIAMOND_SWORD_ATTACK:list(total_sword.sword_attack_generate(DIAMOND_SWORD_ATTACK, DIAMOND_SWORD_ATTACK_DAMAGE)), \
                     NETHERITE_SWORD_ATTACK:list(total_sword.sword_attack_generate(NETHERITE_SWORD_ATTACK, NETHERITE_SWORD_ATTACK_DAMAGE))
                    }

sword_attack_rect_dic = { WOODEN_SWORD_ATTACK_RECT:sword_attack_dic.get(WOODEN_SWORD_ATTACK)[4].get_rect(), \
                          STONE_SWORD_ATTACK_RECT:sword_attack_dic.get(STONE_SWORD_ATTACK)[4].get_rect(), \
                          IRON_SWORD_ATTACK_RECT:sword_attack_dic.get(IRON_SWORD_ATTACK)[4].get_rect(), \
                          GOLDEN_SWORD_ATTACK_RECT:sword_attack_dic.get(GOLDEN_SWORD_ATTACK)[4].get_rect(), \
                          DIAMOND_SWORD_ATTACK_RECT:sword_attack_dic.get(DIAMOND_SWORD_ATTACK)[4].get_rect(), \
                          NETHERITE_SWORD_ATTACK_RECT:sword_attack_dic.get(NETHERITE_SWORD_ATTACK)[4].get_rect()
                        }

sword_attack_running_dic = { WOODEN_SWORD_ATTACK:True, \
                             STONE_SWORD_ATTACK:False, \
                             IRON_SWORD_ATTACK:False, \
                             GOLDEN_SWORD_ATTACK:False, \
                             DIAMOND_SWORD_ATTACK:False, \
                             NETHERITE_SWORD_ATTACK:False
                           }

sword_attack_rect_running_dic = { WOODEN_SWORD_ATTACK_RUNNING_RECT:True, \
                                  STONE_SWORD_ATTACK_RUNNING_RECT:False, \
                                  IRON_SWORD_ATTACK_RUNNING_RECT:False, \
                                  GOLDEN_SWORD_ATTACK_RUNNING_RECT:False, \
                                  DIAMOND_SWORD_ATTACK_RUNNING_RECT:False, \
                                  NETHERITE_SWORD_ATTACK_RUNNING_RECT:False
                                }

sword_list = []
for items in list(sword_dic.keys()):
    sword_list.append(items)

sword_attack_list = []       
for items in list(sword_attack_dic.keys()):
    sword_attack_list.append(items)

sword_attack_rect_dic_list = []
for items in list(sword_attack_rect_dic.keys()):
    sword_attack_rect_dic_list.append(items)


sword_x_pos = sword_dic.get(WOODEN_SWORD)[2]
sword_y_pos = sword_dic.get(WOODEN_SWORD)[3]
sword_attack_x_pos = sword_x_pos
sword_attack_y_pos = sword_y_pos # 어차피 검 사진은 160x160 이므로 sword의 x좌표 y좌표 똑같이 줘도 상관없을듯

sword_running = sword_dic.get(WOODEN_SWORD)
sword_attack_rect_running = True

while running:
    dt = clock.tick(100) # 게임 화면의 초당 프레임 수를 설정
    screen.fill(BLACK)

    # 충돌 처리를 위한 enemy의 rect 정보 업데이트
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

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

                # 어떤 sword가 running 상태인지 확인하고 그 객체를 투명화 및 attack 사진을 출력함.
                sword_running_IfTrue_attack()
                
                # pygame.display.update() # 게임 화면을 다시 그리기
                check_collision()

                enemy_update = False  # 이걸 해야 enemy를 화면에 다시 그릴 수 있음.
                # time.sleep(0.05)
            elif event.key == pygame.K_i:
                pause_msg('Pause', WHITE)
                inventory() # inventory 띄우기
                
        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: to_y = 0
            elif event.key == pygame.K_SPACE:
                detach_spacebar(sword_attack_running_dic)
            elif event.key == pygame.K_a: pass
                
    
    # 현재 활성화된 sword_attack_running에 따라 그에 상응하는 rect 생성
    for sword_attack_rect_name, sword_name in zip(sword_attack_rect_dic_list, sword_attack_list):
        if sword_attack_running_dic.get(sword_name) == True: 
            sword_attack_rect_dic.get(sword_attack_rect_name).left = sword_x_pos
            sword_attack_rect_dic.get(sword_attack_rect_name).top = sword_y_pos

    # sword 객체의 방향키에 따른 이동 속도 조절            
    sword_x_pos += to_x * dt
    sword_y_pos += to_y * dt

    sword_attack_x_pos = sword_x_pos
    sword_attack_y_pos = sword_y_pos

    # sword 객체의 가로 경계값 처리
    if sword_x_pos < 0:
        sword_x_pos = 0
    elif sword_x_pos > screen_width - sword_attack_dic.get(WOODEN_SWORD_ATTACK)[0]:
        sword_x_pos = screen_width - sword_attack_dic.get(WOODEN_SWORD_ATTACK)[0]

    # sword 객체의 세로 경계값 처리
    if sword_y_pos < 0:
        sword_y_pos = 0
    elif sword_y_pos > screen_height - sword_attack_dic.get(WOODEN_SWORD_ATTACK)[1]:
        sword_y_pos = screen_height - sword_attack_dic.get(WOODEN_SWORD_ATTACK)[1]

    screen.blit(background,(0,0)) # 배경 그리기
    
    # 적 체력이 0 이하이면 체력이 다시 200으로 회복
    if enemy_hp <= 0:
        enemy_hp = original_enemy_hp
        enemy_cnt += 1
        for sword_attack_name, sword_name in zip(sword_attack_list, sword_list):
            if sword_attack_running_dic.get(sword_attack_name) == True:
                enemy_money += sword_dic.get(sword_name)[5]
                print(enemy_money)
        enemy_x_pos, enemy_y_pos = random_appear()
        enemy_update == False
    
    # enemy_update가 False 일 때 enemy를 화면에 다시 그리기
    if enemy_update == False:
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
        
    enemy_cnt_running_onoff(enemy_cnt)

    enemy1.hp_bar() # hp 바 생성

    determine_sword_object() # 어떤 sword 객체가 나올지 결정하는 함수

    msg_enemy_money = "money : " + str(enemy_money)
    msg_enemy_cnt = "kill : " + str(enemy_cnt)

    # 게임 오버 메시지
    print_msg(msg_enemy_cnt,40,20,RED)
    print_msg(msg_enemy_money,screen_width-100,20,WHITE)


    pygame.display.update() # 게임 화면을 다시 그리기

pygame.quit()