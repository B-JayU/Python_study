# -*-coding: EUC-KR -*-
import pygame

pygame.init() # �ʱ�ȭ (�ݵ�� �ʿ�)

# ȭ�� ũ�� ����
screen_width = 480;
screen_height = 640;
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("Byju_yu Game") # ���� �̸�

# ��� �̹��� �ҷ�����
background = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/background.jpeg")

# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running:
    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�

    screen.fill((0,140,200))
    #screen.blit(background, (0,0)) # ��� �׸���
    pygame.display.update() # ����ȭ���� �ٽ� �׸���!
# pygame ����
pygame.quit()

