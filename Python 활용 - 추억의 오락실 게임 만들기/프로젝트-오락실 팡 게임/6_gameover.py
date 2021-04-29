# -*-coding: EUC-KR -*-
# 1. ��� ���� ���ָ� ���� ���� (����)
# 2. ĳ���ʹ� ���� ������ ���� ���� (����)
# 3. �ð� ���� 99�� �ʰ� �� ���� ���� (����)




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
ball_speed_y = [-12, -10, -8, -6] # intdex 0, 1, 2, 3 �� �ش��ϴ� ��

# ��
balls = []

balls.append({
    "pos_x" : 50, # ���� x��ǥ
    "pos_y" : 50, # ���� y��ǥ
    "img_idx" : 0, # ���� �̹��� �ε���
    "to_x" : 3, # x�� �̵� ����, -3 �̸� ��������, 3 �̸� ����������
    "to_y" : -6, # y�� �̵�����,
    "init_spd_y": ball_speed_y[0]}) # ���� ���� �ӵ�

# ����� ����, �� ���� ���� ����
weapon_to_remove = -1
ball_to_remove = -1

# Font ����
game_font = pygame.font.Font(None, 48)
total_time = 10
start_ticks = pygame.time.get_ticks() # ���� �ð� ����

# ���� ���� �޽���
# TimeOut(�ð� �ʰ� ����)
# Mission Complete(����)
# Game Over (ĳ���� ���� ����, ����)
game_result = "Game Over"

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
            ball_val["to_y"] += 0.2

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. �浹 ó��

    # ĳ���� rect ���� ������Ʈ
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # �� rect ���� ������Ʈ
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # ���� ĳ���� �浹 üũ
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # ���� �����  �浹 ó��
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # ���� rect ���� ������Ʈ
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # �浹 üũ
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # �ش� ���� ���ֱ� ���� �� ����
                ball_to_remove = ball_idx  # �ش� �� ���ֱ� ���� �� ����
                
                # ���� ���� ũ���� ���� �ƴ϶�� ���� �ܰ��� ������ �����ֱ�
                if ball_img_idx < 3:
                    # ���� �� ũ�� ������ ������ ��
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # ������ �� ����
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # �������� ƨ�ܳ����� ���� ��
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # ���� x��ǥ
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # ���� y��ǥ
                        "img_idx" : ball_img_idx + 1, # ���� �̹��� �ε���
                        "to_x" : -3, # x�� �̵� ����, -3 �̸� ��������, 3 �̸� ����������
                        "to_y" : -6, # y�� �̵�����,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]}) # ���� ���� �ӵ�

                    # ���������� ƨ�ܳ����� ���� ��
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # ���� x��ǥ
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # ���� y��ǥ
                        "img_idx" : ball_img_idx + 1, # ���� �̹��� �ε���
                        "to_x" : 3, # x�� �̵� ����, -3 �̸� ��������, 3 �̸� ����������
                        "to_y" : -6, # y�� �̵�����,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]}) # ���� ���� �ӵ�
                break
        
    # �浹�� �� or ���� ���ֱ�
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # ��� ���� ���� ��� ���� ���� (����)
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    
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

    # ��� �ð� ���
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # �ð� �ʰ��ߴٸ�
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update() 

# ���� ���� �޽���
msg = game_font.render(game_result, True, (255, 255, 0)) # ��������� ����
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 5�� ���
pygame.time.delay(5000)

pygame.quit()

