# -*-coding: EUC-KR -*-
# Quiz) �ϴÿ��� �������� �� ���ϱ� ������ ����ÿ�.

# [���� ����]
# 1. ĳ���ʹ� ȭ�� ���� �Ʒ��� ��ġ, �¿�θ� �̵� ����
# 2. ���� ȭ�� ���� ������ ������. x ��ǥ�� �Ź� �������� ����
# 3. ĳ���Ͱ� ���� ���ϸ� ���� ���� �ٽ� ������
# 4. ĳ���Ͱ� �˰� �浹�ϸ� ���� ����
# 5. FPS �� 30 ���� ����

# [���� �̹���]
# 1. ��� 640 * 480 (���� ����) - background.png
# 2. ĳ���� : 70 * 70 - character.png
# 3. �� : 70 * 70 - enemy_shit.png

import pygame
import random
# �⺻ �ʱ�ȭ (�ݵ�� �ؾ� �ϴ� �͵�)
pygame.init()

# ȭ�� ũ�� ����
screen_width = 640 # ���� ũ��
screen_height = 480 # ���� ũ��
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()

# 1. ����� ���� �ʱ�ȭ ( ��� ȭ��, ���� �̹���, ��ǥ, �ӵ�, ��Ʈ ��)
# ��� �����
background = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/background.png")

# ĳ���� �����
character = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/character.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# �̵� ��ġ
to_x = 0
character_speed = 10

# �� �����
ddong = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/enemy_shit.jpeg")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10


running = True
while running:
    dt = clock.tick(30)

    # 2. �̺�Ʈ ó�� (Ű����, ���콺 ��)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 3. ���� ĳ���� ��ġ ����
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
    
    # 4. �浹 ó��
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("�浹�߽��ϴ�.")
        running = False


    # 5. ȭ�鿡 �׸���
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))


    pygame.display.update()

pygame.quit()





