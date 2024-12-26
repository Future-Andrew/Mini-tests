import pygame
import time
import random
import tkinter as tk

# 初始化pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (165, 42, 42)  # 褐色

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

def our_snake(snake_block, snake_list, color):
    """绘制蛇"""
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def show_score(color, score, y_offset):
    """显示分数"""
    score_surface = score_font.render(f"{score}", True, color)
    dis.blit(score_surface, [10, y_offset])

def game_over(message):
    """游戏结束界面"""
    dis.fill(blue)
    game_over_surface = font_style.render(message, True, white)
    dis.blit(game_over_surface, (dis_width / 6, dis_height / 3))
    pygame.display.update()
    pygame.time.wait(3000)  # 等待3秒

def game_loop(num_players):
    snake1 = [(100, 50)]
    snake1_dir = "RIGHT"
    snake1_speed = 15
    snake1_length = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    score1 = 0

    if num_players == 2:
        snake2 = [(300, 50)]
        snake2_dir = "UP"
        snake2_speed = 15
        snake2_length = 1
        score2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if num_players == 1:
                    if event.key == pygame.K_LEFT:
                        snake1_dir = "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        snake1_dir = "RIGHT"
                    elif event.key == pygame.K_UP:
                        snake1_dir = "UP"
                    elif event.key == pygame.K_DOWN:
                        snake1_dir = "DOWN"
                elif num_players == 2:
                    if event.key == pygame.K_LEFT:
                        snake2_dir = "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        snake2_dir = "RIGHT"
                    elif event.key == pygame.K_UP:
                        snake2_dir = "UP"
                    elif event.key == pygame.K_DOWN:
                        snake2_dir = "DOWN"
                    elif event.key == pygame.K_a:
                        snake1_dir = "LEFT"
                    elif event.key == pygame.K_d:
                        snake1_dir = "RIGHT"
                    elif event.key == pygame.K_w:
                        snake1_dir = "UP"
                    elif event.key == pygame.K_s:
                        snake1_dir = "DOWN"

        # 蛇1移动
        if snake1_dir == "LEFT":
            snake1[0] = (snake1[0][0] - snake_block, snake1[0][1])
        elif snake1_dir == "RIGHT":
            snake1[0] = (snake1[0][0] + snake_block, snake1[0][1])
        elif snake1_dir == "UP":
            snake1[0] = (snake1[0][0], snake1[0][1] - snake_block)
        elif snake1_dir == "DOWN":
            snake1[0] = (snake1[0][0], snake1[0][1] + snake_block)

        # 蛇2移动
        if num_players == 2:
            if snake2_dir == "LEFT":
                snake2[0] = (snake2[0][0] - snake_block, snake2[0][1])
            elif snake2_dir == "RIGHT":
                snake2[0] = (snake2[0][0] + snake_block, snake2[0][1])
            elif snake2_dir == "UP":
                snake2[0] = (snake2[0][0], snake2[0][1] - snake_block)
            elif snake2_dir == "DOWN":
                snake2[0] = (snake2[0][0], snake2[0][1] + snake_block)

        # 蛇1吃到食物
        if snake1[0] == (foodx, foody):
            score1 += 1
            snake1.append(snake1[-1])
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        # 蛇2吃到食物
        if num_players == 2 and snake2[0] == (foodx, foody):
            score2 += 1
            snake2.append(snake2[-1])
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        # 蛇1撞墙或撞到自己
        if (snake1[0][0] < 0 or snake1[0][0] > dis_width - snake_block or
                snake1[0][1] < 0 or snake1[0][1] > dis_height - snake_block or
                snake1[0] in snake1[1:]):
            game_over("Game Over!")
            return

        # 蛇2撞墙或撞到自己
        if num_players == 2 and (snake2[0][0] < 0 or snake2[0][0] > dis_width - snake_block or
                snake2[0][1] < 0 or snake2[0][1] > dis_height - snake_block or
                snake2[0] in snake2[1:]):
            game_over("Snake 1 Wins!")
            return

        # 蛇相撞
        if num_players == 2 and snake1[0] in snake2:
            game_over("Snake 2 Wins!")
            return
        if num_players == 2 and snake2[0] in snake1:
            game_over("Snake 1 Wins!")
            return

        dis.fill(blue)
        show_score(white, score1, 10)
        if num_players == 2:
            show_score(white, score2, dis_height - 50)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        our_snake(snake_block, snake1, brown)
        if num_players == 2:
            our_snake(snake_block, snake2, blue)
        pygame.display.update()

        clock.tick(snake_speed)

# Tkinter部分
def run_game():
    root = tk.Tk()
    root.title("游戏模式选择")

    def start_single_player():
        root.destroy()
        start_game(1)

    def start_multi_player():
        root.destroy()
        start_game(2)

    single_player_button = tk.Button(root, text="单人模式", command=start_single_player)
    single_player_button.pack(pady=20)

    multi_player_button = tk.Button(root, text="双人模式", command=start_multi_player)
    multi_player_button.pack(pady=20)

    root.mainloop()

def start_game(num_players):
    # 创建倒计时开始界面
    start_root = tk.Tk()
    start_root.title("游戏即将开始")

    def count_down():
        nonlocal count
        count -= 1
        count_label.config(text=f"{count}秒后开始")
        if count <= 0:
            start_root.destroy()
            game_loop(num_players)
        else:
            start_root.after(1000, count_down)

    count = 5
    count_label = tk.Label(start_root, text=f"{count}秒后开始")
    count_label.pack(pady=20)
    start_root.after(1000, count_down)

run_game()