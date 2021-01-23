import pygame

pygame.init()

screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("검 키우기") # 게임 이름

running = True
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

enemy_hp = 500
while running:

    pygame.draw.rect(screen, RED, (200,250,250,5))

    pygame.draw.rect(screen, GREEN, (200,250,(enemy_hp//2),5))

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("dd")
                enemy_hp -= 20

    pygame.display.update()

pygame.quit()