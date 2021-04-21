# -*-coding: EUC-KR -*-
import pygame

pygame.init() # �ʱ�ȭ (�ݵ�� �ʿ�)

# ȭ�� ũ�� ����
screen_width = 980;
screen_height = 640;
screen = pygame.display.set_mode((screen_width, screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("�����ϴµ� ����������!!!") # ���� �̸�

# ��� �̹��� �ҷ�����
background = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/background.jpeg")

# ��������Ʈ(ĳ����) �ҷ�����
character = pygame.image.load("/Users/mac/Desktop/python/Python Ȱ�� - �߾��� ������ ���� �����/pygame_basic/byju_character.jpeg")
character_size = character.get_rect().size # �̹����� ũ�⸦ ����
character_width = character_size[0] # ĳ������ ���� ũ��
character_height = character_size[1] # ĳ������ ���� ũ��
character_x_pos = screen_width/2-character_width/2 # ȭ�� ������ ���� ũ�⿡ �ش��ϴ� ���� ��ġ (������ġ)
character_y_pos = screen_height-character_height # ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ���� ��ġ (������ġ)

# �̵��� ��ǥ
to_x = 0
to_y = 0
# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running:
    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�
        
        # Ű���� �̺�Ʈ�� �߻��� ���
        if event.type == pygame.KEYDOWN: # Ű���� Ű�� ������ ��
            if event.key == pygame.K_LEFT: # Ű���� ���� Ű 
                to_x -= 1
            elif event.key == pygame.K_RIGHT: # Ű���� ������ Ű
                to_x += 1
            elif event.key == pygame.K_UP: # Ű���� ���� Ű
                to_y -= 1
            elif event.key == pygame.K_DOWN: # Ű���� �Ʒ��� Ű
                to_y += 1
        
        if event.type == pygame.KEYUP: # ����Ű�� ���� ����
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

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

    screen.fill((0,140,200))
    #screen.blit(background, (0,0)) # ��� �׸���
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # ����ȭ���� �ٽ� �׸���!

# pygame ����
pygame.quit()

