from tkinter import *
import os
import sys
import pygame

pygame.init()

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
         if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
             running = False # 게임이 진행중이 아님

pygame.quit()