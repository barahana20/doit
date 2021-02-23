import tkinter as tk
import pygame

def inventory():
    import tkinter as tk
    root = tk.Tk ()
    root.geometry ("200x100")
    lbl = tk.Label (text ='LABEL')
    btn = tk.Button (text ='PUSH')
    lbl.pack ()
    btn.pack ()
    tk.mainloop ()

def pause_msg(PAUSE, color):
    msg = pause_font.render(PAUSE, True, color) # 검은색
    width = (screen_width // 2)
    height = (screen_height // 2)
    msg_rect = msg.get_rect(center=(width,height))
    screen.blit(msg, msg_rect)
    pygame.display.update()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)


pygame.init()

screen_width = 640 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("검 키우기") # 게임 이름

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
pause_font = pygame.font.Font(None, 100)

running = 1
while running:
    screen.fill(BLACK)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?

            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                running = False # 게임이 진행중이 아님

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    if __name__ == "__main__":
                        
                        pause_msg('Pause', WHITE)
                        inventory() # inventory 띄우기
                    
            if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
                if event.key == pygame.K_i: pass

pygame.quit()