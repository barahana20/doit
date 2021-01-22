wooden_sword = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/wooden_sword.png")
wooden_sword_leaf = wooden_sword.get_rect()
wooden_sword_size = wooden_sword.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_width = wooden_sword_size[0] # 캐릭터의 가로 크기
wooden_sword_height = wooden_sword_size[1] # 캐릭터의 세로 크기
wooden_sword_x_pos = (screen_width-wooden_sword_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
wooden_sword_y_pos = screen_height - wooden_sword_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

wooden_sword_attack = pygame.image.load("C:/doit/그냥 심심할 떄 코딩하는 곳/간단하게 만드는 게임/images/wooden_sword_attack.png")
wooden_sword_attack_size = wooden_sword_attack.get_rect().size # 이미지의 크기를 구해옴
wooden_sword_attack_width = wooden_sword_attack_size[0] # 캐릭터의 가로 크기
wooden_sword_attack_height = wooden_sword_attack_size[1] # 캐릭터의 세로 크기
wooden_sword_attack_x_pos = wooden_sword_x_pos
wooden_sword_attack_y_pos = wooden_sword_y_pos


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