# -*-coding: EUC-KR -*-
import pygame

pygame.init() # �ʱ�ȭ (�ݵ�� �ʿ�)

# ȭ�� ũ�� ����
screen_width = 480;
screen_height = 640;
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("Byju_yu Game") # ���� �̸�

# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running:
    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�

# pygame ����
pygame.quit()

