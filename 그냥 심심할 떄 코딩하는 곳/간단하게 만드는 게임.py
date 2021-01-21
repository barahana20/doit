from tkinter import *
import os
import sys
import pygame

class Weapon:
    pass

class Sword(Weapon):
    def __init__(self, money, damage):
        self.money = money
        self.damage = damage

    def wooden_sword(self):
        print("나무 검")
    def stone_sword(self):
        print("돌 검")  
    def iron_sword(self):
        print("철 검")
    def golden_sword(self):
        print("금 검")
    def diamond_sword(self):
        print("다이아몬드 검")
    def netherite_sword(self):
        print("네더라이트 검")
sword = Sword(10,20)
sword.iron_sword()
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