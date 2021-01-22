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
    def __init__(self, money, damage, speed):
        self.money = money
        self.damage = damage
        self.speed = speed
        print("Sward 클래스가 호출되었습니다")

    def wooden_sword(self):
        self.money = 1000
        self.damage = 4
        print("나무 검")
    def stone_sword(self):
        self.money = 2000
        self.damage = 5
        print("돌 검")  
    def iron_sword(self):
        self.money = 4000
        self.damage = 7
        print("철 검")
    def golden_sword(self):
        self.money = 8000
        self.damage = 9
        print("금 검")
    def diamond_sword(self):
        self.money = 16000
        self.damage = 11
        print("다이아몬드 검")
    def netherite_sword(self):
        self.money = 32000
        self.damage = 15
        print("네더라이트 검")
    def attack_effect(self):
        pass

def random_appear():
    a = random.randint(0,screen_width-enemy_width)
    b = random.randint(0,screen_height-enemy_height)
    return (a,b)

pygame.init()

screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("검 키우기") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/doit/funny_coding/simple_game/images/background.png")

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/doit/funny_coding/simple_game/images/normal_zombie.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width-enemy_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)# 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
enemy_money = 0
enemy_hp = 0


wooden_sword1 = Sword(1,2,3)
wooden_sword1.wooden_sword()
zombie1 = Zombie(enemy_money, enemy_hp)
zombie1.normal_zombie()

#FPS
clock = pygame.time.Clock()

# 이동 속도
wooden_sword_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)


wooden_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/wooden_sword.png")
wooden_sword_leaf = wooden_sword.get_rect()
wooden_sword_size = wooden_sword.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_width = wooden_sword_size[0] # 캐릭터의 가로 크기
wooden_sword_height = wooden_sword_size[1] # 캐릭터의 세로 크기
wooden_sword_x_pos = (screen_width-wooden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
wooden_sword_y_pos = screen_height - wooden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

wooden_sword_attack = pygame.image.load("C:/doit/funny_coding/simple_game/images/wooden_sword_attack.png")
wooden_sword_attack_size = wooden_sword_attack.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_attack_width = wooden_sword_attack_size[0] # 캐릭터의 가로 크기
wooden_sword_attack_height = wooden_sword_attack_size[1] # 캐릭터의 세로 크기
wooden_sword_attack_x_pos = wooden_sword_x_pos
wooden_sword_attack_y_pos = wooden_sword_y_pos


# iron_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/iron_sword.png")
# iron_sword_size = iron_sword.get_rect().size # 이미지의 크기를 구해옴
# iron_sword_width = iron_sword_size[0] # 캐릭터의 가로 크기
# iron_sword_height = iron_sword_size[1] # 캐릭터의 세로 크기
# iron_sword_x_pos = (screen_width-iron_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# iron_sword_y_pos = screen_height - iron_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# stone_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/stone_sword.png")
# stone_sword_size = stone_sword.get_rect().size # 이미지의 크기를 구해옴
# stone_sword_width = stone_sword_size[0] # 캐릭터의 가로 크기
# stone_sword_height = stone_sword_size[1] # 캐릭터의 세로 크기
# stone_sword_x_pos = (screen_width-stone_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# stone_sword_y_pos = screen_height - stone_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# golden_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/golden_sword.png")
# golden_sword_size = golden_sword.get_rect().size # 이미지의 크기를 구해옴
# golden_sword_width = golden_sword_size[0] # 캐릭터의 가로 크기
# golden_sword_height = golden_sword_size[1] # 캐릭터의 세로 크기
# golden_sword_x_pos = (screen_width-golden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# golden_sword_y_pos = screen_height - golden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# diamond_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/diamond_sword.png")
# diamond_sword_size = diamond_sword.get_rect().size # 이미지의 크기를 구해옴
# diamond_sword_width = diamond_sword_size[0] # 캐릭터의 가로 크기
# diamond_sword_height = diamond_sword_size[1] # 캐릭터의 세로 크기
# diamond_sword_x_pos = (screen_width-diamond_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# diamond_sword_y_pos = screen_height - diamond_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# netherite_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/netherite_sword.png")
# netherite_sword_size = netherite_sword.get_rect().size # 이미지의 크기를 구해옴
# netherite_sword_width = netherite_sword_size[0] # 캐릭터의 가로 크기
# netherite_sword_height = netherite_sword_size[1] # 캐릭터의 세로 크기
# netherite_sword_x_pos = (screen_width-netherite_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# netherite_sword_y_pos = screen_height - netherite_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

running = True

to_x = 0
to_y = 0
transparent = (0, 0, 0, 0)
enemy_remove = False
enemy_cnt = 0


while running:
    dt = clock.tick(100) # 게임 화면의 초당 프레임 수를 설정
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
                print("스페이스바를 눌렀습니다.")
                wooden_sword.fill(transparent)
                screen.blit(background,(0,0)) # 배경 그리기
                screen.blit(wooden_sword_attack, (wooden_sword_x_pos, wooden_sword_y_pos))

                # 충돌 체크
                if wooden_sword_rect.colliderect(enemy_rect):
                    print("충돌했어요")
                    enemy_remove = True
                    enemy_x_pos, enemy_y_pos = random_appear()
                    
                    enemy_cnt += 1
                enemy_remove = False    
                
                pygame.display.update() # 게임 화면을 다시 그리기

                time.sleep(0.05)

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_SPACE:
                wooden_sword = pygame.image.load("C:/doit/funny_coding/simple_game/images/wooden_sword.png")
                # pygame.display.update() # 게임 화면을 다시 그리기
                print("wooden_sword 객체를 다시 소환했습니다")
                
    wooden_sword_x_pos += to_x * dt
    wooden_sword_y_pos += to_y * dt

    # 가로 경계값 처리
    if wooden_sword_x_pos < 0:
        wooden_sword_x_pos = 0
    elif wooden_sword_x_pos > screen_width - wooden_sword_width:
        wooden_sword_x_pos = screen_width - wooden_sword_width

    # 세로 경계값 처리
    if wooden_sword_y_pos < 0:
        wooden_sword_y_pos = 0
    elif wooden_sword_y_pos > screen_height - wooden_sword_height:
        wooden_sword_y_pos = screen_height - wooden_sword_height

    

    # 충돌 처리를 위한 rect 정보 업데이트
    wooden_sword_rect = wooden_sword.get_rect()
    wooden_sword_rect.left = wooden_sword_x_pos
    wooden_sword_rect.top = wooden_sword_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
        
    screen.blit(background,(0,0)) # 배경 그리기

    if enemy_remove == False:
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 

    screen.blit(wooden_sword, (wooden_sword_x_pos, wooden_sword_y_pos))
    
    kill_enemy_cnt = "kill : " + str(enemy_cnt)
    # 게임 오버 메시지
    msg = game_font.render(kill_enemy_cnt, True, (0,0,0)) # 노란색
    msg_rect = msg.get_rect(center=(40,20))
    screen.blit(msg, msg_rect)

    pygame.display.update() # 게임 화면을 다시 그리기

pygame.quit()