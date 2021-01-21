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
    def __init__(self, money, damage):
        self.money = money
        self.money = damage

class Sword(Weapon):
    def __init__(self, money, damage):
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

sword = Sword(10,20)
zombie = Zombie(10,20)
Zombie.normal_zombie
# pygame.init()
# root.geometry()


# screen_width = 480 # 가로 크기
# screen_height = 640 # 세로 크기
# pygame.display.set_mode((screen_width, screen_height))

# running = True
# while running:
#     for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
#          if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
#              running = False # 게임이 진행중이 아님

# pygame.quit()