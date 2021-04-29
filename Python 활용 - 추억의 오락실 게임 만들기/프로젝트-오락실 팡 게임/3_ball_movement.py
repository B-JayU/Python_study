# -*-coding: EUC-KR -*-
import pygame
#############################################################################################
# �⺻ �ʱ�ȭ (�ݵ�� �ؾ� �ϴ� �͵�)
pygame.init() 

# ȭ�� ũ�� ����
screen_width = 640 # ���� ũ��
screen_height = 480 # ���� ũ��
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("BJ Pang") 

# FPS
clock = pygame.time.Clock()
#############################################################################################

# 1. ����� ���� �ʱ�ȭ (��� ȭ��, ���� �̹���, ��ǥ, �ӵ�, ��Ʈ ��)
# current_path = os.path.dirname(__file__) # ���� ������ ��ġ ��ȯ
# image_path = os.path.join(current_path, "images") # imgaes ���� ��ġ ��ȯ

background = pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/background.png")

# �������� �����
stage = pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1] # �������� ���� ���� ĳ���͸� �α� ���� ���

# ĳ���� �����
character = pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2 )
character_y_pos = screen_height - character_height - stage_height

# ĳ���� �̵� ����
character_to_x = 0

# ĳ���� �̵� �ӵ�
character_speed = 5

# ���� �����
weapon = pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# ����� �� ���� ���� �� �߻� ����
weapons = []

# ���� �̵� �ӵ� 
weapon_speed = 10

# �� ����� (4�� ũ�⿡ ���� �������� ó��)
ball_images = [
    # �� ���� �ӵ��� Ƣ������� ���̰� �ٸ���
    pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/balloon1.png"),
    pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/ballon2.png"),
    pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/ballon3.png"),
    pygame.image.load("/Users/mac/Desktop/python/������Ʈ-������ �� ����/images/ballon4.png")
]

# �� ũ�⿡ ���� ���� ���ǵ�
ball_speed_y = [-18, -15, -12, -9] # intdex 0, 1, 2, 3 �� �ش��ϴ� ��

# ��
balls = []

balls.append({
    "pos_x" : 50, # ���� x��ǥ
    "pos_y" : 50, # ���� y��ǥ
    "img_idx" : 0, # ���� �̹��� �ε���
    "to_x" : 3, # x�� �̵� ����, -3 �̸� ��������, 3 �̸� ����������
    "to_y" : -6, # y�� �̵�����,
    "init_spd_y": ball_speed_y[0]}) # ���� ���� �ӵ�


running = True 
while running:
    dt = clock.tick(60) 

    # 2. �̺�Ʈ ó�� (Ű����, ���콺 ��)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # ���� �߻�
                weapon_x_pos = character_x_pos + (character_width/2)-(weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    # 3. ���� ĳ���� ��ġ ����
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # ���� ��ġ ����
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # ���� ��ġ�� ����

    # õ�忡 ���� ���� ���ֱ�
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # �� ��ġ ����
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # ���κ��� ����� �� �� �̵� ��ġ ���� (ƨ�� ������ ȿ��)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1 

        # ���� ��ġ
        # ���������� ƨ�ܼ� �ö󰡴� ó��
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # �� ���� ��� ��쿡�� �ӵ��� ���� (�ӵ��� ������ ������ ������ �����Ѵ�.)
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. �浹 ó��

    
    # 5. ȭ�鿡 �׸���
    screen.blit(background, (0, 0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        balls_pos_x = val["pos_x"]
        balls_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (balls_pos_x, balls_pos_y))

    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    
    pygame.display.update() 

pygame.quit()

