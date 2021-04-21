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

# ��������Ʈ(ĳ����) �ҷ�����
character = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/character.jpg")
character_size = character.get_rect().size # �̹����� ũ�⸦ ����
character_width = character_size[0] # ĳ������ ���� ũ��
character_height = character_size[1] # ĳ������ ���� ũ��
character_x_pos = screen_width/2-character_width/2 # ȭ�� ������ ���� ũ�⿡ �ش��ϴ� ���� ��ġ (������ġ)
character_y_pos = screen_height-character_height # ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ���� ��ġ (������ġ)


# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running:
    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�

    screen.fill((0,140,200))
    #screen.blit(background, (0,0)) # ��� �׸���
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # ����ȭ���� �ٽ� �׸���!

# pygame ����
pygame.quit()

