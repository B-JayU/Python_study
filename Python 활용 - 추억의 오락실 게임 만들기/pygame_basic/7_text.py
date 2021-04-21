# -*-coding: EUC-KR -*-
import pygame

pygame.init() # �ʱ�ȭ (�ݵ�� �ʿ�)

# ȭ�� ũ�� ����
screen_width = 980;
screen_height = 720;
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("�����ϴµ� ����������!!!") # ���� �̸�

# FPS
clock = pygame.time.Clock()

# ��� �̹��� �ҷ�����
background = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/background.jpeg")

# ��������Ʈ(ĳ����) �ҷ�����
character = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/byju_character.jpeg")
character_size = character.get_rect().size # �̹����� ũ�⸦ ����
character_width = character_size[0] # ĳ������ ���� ũ��
character_height = character_size[1] # ĳ������ ���� ũ��
character_x_pos = screen_width/2-character_width/2 # ȭ�� ������ ���� ũ�⿡ �ش��ϴ� ���� ��ġ (������ġ)
character_y_pos = screen_height-character_height # ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ���� ��ġ (������ġ)

# ĳ���� �⺻ �̵� �ӵ�
character_speed = 0.5
# �̵��� ��ǥ
to_x = 0
to_y = 0

# �� enemy ĳ����
enemy = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/Enemy.jpg")
enemy_size = enemy.get_rect().size # �̹����� ũ�⸦ ����
enemy_width = enemy_size[0] # ĳ������ ���� ũ��
enemy_height = enemy_size[1] # ĳ������ ���� ũ��
enemy_x_pos = (screen_width/2) - (enemy_width/2) # ȭ�� ������ ���� ũ�⿡ �ش��ϴ� ���� ��ġ (������ġ)
enemy_y_pos = (screen_width/2) - (enemy_width/2) # ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ���� ��ġ (������ġ)

# ��Ʈ ����
game_font = pygame.font.Font(None, 40)

# ���� �� �ð�
total_time = 60

# ���� �ð� ����
start_ticks = pygame.time.get_ticks() # ���� tick �� �޾ƿ�

# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running:
    dt = clock.tick(100) # ����ȭ���� �ʴ� ������ ���� ����
    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�
        
        # Ű���� �̺�Ʈ�� �߻��� ���
        if event.type == pygame.KEYDOWN: # Ű���� Ű�� ������ ��
            if event.key == pygame.K_LEFT: # Ű���� ���� Ű 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # Ű���� ������ Ű
                to_x += character_speed
            elif event.key == pygame.K_UP: # Ű���� ���� Ű
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # Ű���� �Ʒ��� Ű
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # ����Ű�� ���� ����
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # ���� ��谪 ó��
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    # ���� ��谪 ó��
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # �浹 ó��
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #�浹 üũ
    if character_rect.colliderect(enemy_rect):
        # msgbox("�浹�� �߻��Ͽ����ϴ�.")
        print("�浹�� �߻��Ͽ����ϴ�.")
        running = False
    
    screen.fill((0,140,200))
    #screen.blit(background, (0,0)) # ��� �׸���
    screen.blit(character, (character_x_pos, character_y_pos)) # ĳ���� �׸���
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #  �� �׸���
    
    # Ÿ�̸� ���� �ֱ�
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000 
    # �氡 �ð�(ms)dmf 1000���� ����� ��(s) ������ ǥ��

    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255, 255, 255))
    # ����� ����, True, ���� ����
    screen.blit(timer, (10, 10))

    # ���� �ð��� 0 �����̸� ���� ����
    if total_time - elapsed_time <= 0:
        print("Ÿ�� �ƿ�")
        running = False

    pygame.display.update() # ����ȭ���� �ٽ� �׸���!

# pygame ����
pygame.quit()

