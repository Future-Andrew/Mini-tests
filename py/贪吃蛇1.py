import pygame
import time
import random

pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 创建游戏窗口
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃蛇游戏')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 2 + y_offset])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    start_time = time.time()

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # 显示时间和蛇的长度
        elapsed_time = int(time.time() - start_time)
        time_str = f"Time: {elapsed_time}s"
        length_str = f"Length: {Length_of_snake}"
        time_render = score_font.render(time_str, True, white)
        length_render = score_font.render(length_str, True, white)
        dis.blit(time_render, (10, 10))
        dis.blit(length_render, (dis_width - length_render.get_width() - 10, 10))

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

        if game_close:
            game_over = True

    pygame.quit()
    return elapsed_time, Length_of_snake

def game_over_screen(elapsed_time, Length_of_snake):
    game_over = False

    while not game_over:
        dis.fill(blue)
        message("Game Over", red, y_offset=-50)
        message(f"Time: {elapsed_time}s", white, y_offset=-20)
        message(f"Length: {Length_of_snake}", white, y_offset=10)
        message("Press Q-Quit or C-Play Again", white, y_offset=40)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                if event.key == pygame.K_c:
                    game_over = True
                    return True  # 返回True表示重新开始游戏

    return False  # 返回False表示退出游戏

# 主游戏循环
while True:
    elapsed_time, Length_of_snake = gameLoop()
    if not game_over_screen(elapsed_time, Length_of_snake):
        break