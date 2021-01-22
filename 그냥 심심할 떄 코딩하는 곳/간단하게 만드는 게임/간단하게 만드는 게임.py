from tkinter import *
import os
import sys
import pygame

class Enemy:
    def __init__(self, money, hp):
        self.money = money
        self.hp = hp
        print("enemy 객체가 호출되었습니다")
class Zombie(Enemy):
    def __init__(self, money, hp):
        Enemy.__init__(self, money, hp)
        print("Zombie 객체가 호출되었습니다")

    def normal_zombie(self):
        print("normal_zombie 객체가 호출되었습니다")
                
class Weapon:
    def __init__(self, money, damage, speed):
        self.money = money
        self.money = damage
        self.speed = speed

class Sword(Weapon):
    def __init__(self, money, damage, speed):
        Weapon.__init__(self, money, damage)
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

    def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
        w, h       = image.get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)

        # rotate and blit the image
        surf.blit(rotated_image, origin)


# sword = Sword(10,20)
# zombie = Zombie(10,20)
# Zombie.normal_zombie

pygame.init()

screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("검 키우기") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/background.png")

#FPS
clock = pygame.time.Clock()

# 이동 속도
wooden_sword_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)


wooden_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/wooden_sword.png")
wooden_sword_size = wooden_sword.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_width = wooden_sword_size[0] # 캐릭터의 가로 크기
wooden_sword_height = wooden_sword_size[1] # 캐릭터의 세로 크기
wooden_sword_x_pos = (screen_width-wooden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
wooden_sword_y_pos = screen_height - wooden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

iron_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/iron_sword.png")
iron_sword_size = iron_sword.get_rect().size # 이미지의 크기를 구해옴
iron_sword_width = iron_sword_size[0] # 캐릭터의 가로 크기
iron_sword_height = iron_sword_size[1] # 캐릭터의 세로 크기
iron_sword_x_pos = (screen_width-iron_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
iron_sword_y_pos = screen_height - iron_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

stone_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/stone_sword.png")
stone_sword_size = stone_sword.get_rect().size # 이미지의 크기를 구해옴
stone_sword_width = stone_sword_size[0] # 캐릭터의 가로 크기
stone_sword_height = stone_sword_size[1] # 캐릭터의 세로 크기
stone_sword_x_pos = (screen_width-stone_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
stone_sword_y_pos = screen_height - stone_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

golden_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/golden_sword.png")
golden_sword_size = golden_sword.get_rect().size # 이미지의 크기를 구해옴
golden_sword_width = golden_sword_size[0] # 캐릭터의 가로 크기
golden_sword_height = golden_sword_size[1] # 캐릭터의 세로 크기
golden_sword_x_pos = (screen_width-golden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
golden_sword_y_pos = screen_height - golden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

diamond_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/diamond_sword.png")
diamond_sword_size = diamond_sword.get_rect().size # 이미지의 크기를 구해옴
diamond_sword_width = diamond_sword_size[0] # 캐릭터의 가로 크기
diamond_sword_height = diamond_sword_size[1] # 캐릭터의 세로 크기
diamond_sword_x_pos = (screen_width-diamond_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
diamond_sword_y_pos = screen_height - diamond_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

netherite_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/netherite_sword.png")
netherite_sword_size = netherite_sword.get_rect().size # 이미지의 크기를 구해옴
netherite_sword_width = netherite_sword_size[0] # 캐릭터의 가로 크기
netherite_sword_height = netherite_sword_size[1] # 캐릭터의 세로 크기
netherite_sword_x_pos = (screen_width-netherite_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
netherite_sword_y_pos = screen_height - netherite_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
running = True

to_x = 0
to_y = 0
angle = 0
w, h = wooden_sword.get_size()

while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
             running = False # 게임이 진행중이 아님

        pos = (screen.get_width()//2, screen.get_height()//2)
        pos = (200, 200)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 왼쪽
                to_x -= wooden_sword_speed
            elif event.key == pygame.K_RIGHT: # 오른쪽
                to_x += wooden_sword_speed
            elif event.key == pygame.K_UP: # 위쪽
                to_y -= wooden_sword_speed
            elif event.key == pygame.K_DOWN: # 아래쪽
                to_y += wooden_sword_speed
            elif event.key == pygame.K_SPACE: # 아래쪽
                screen.blit(wooden_sword, (wooden_sword_x_pos, wooden_sword_y_pos))

                Sword.blitRotate(screen, wooden_sword, pos, (w//2, h//2), angle)
                angle += 1

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event. key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
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
    screen.blit(background,(0,0)) # 배경 그리기

    

   

    pygame.display.flip()


    pygame.display.update() # 게임 화면을 다시 그리기

pygame.quit()