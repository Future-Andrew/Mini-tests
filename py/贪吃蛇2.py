import pygame
import time
import random
import tkinter as tk
from tkinter import messagebox

# Pygame部分
def run_pygame_game():
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

    def gameLoop():
        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        start_time = time.time()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return  # 退出游戏
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

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 or snake_list.count([x1, y1]) > 1:
                return  # 游戏结束，退出gameLoop

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
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > Length_of_snake:
                snake_list.pop(0)

            for x in snake_list[:-1]:
                if x == snake_head:
                    return  # 游戏结束，退出gameLoop

            our_snake(snake_block, snake_list)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

    gameLoop()
    pygame.quit()

# Tkinter部分
class GameOverWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Over - 贪吃蛇")

        self.start_button = tk.Button(root, text="继续游戏", command=self.start_game)
        self.start_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="退出游戏", command=self.quit_game)
        self.quit_button.pack(pady=20)

    def start_game(self):
        self.root.destroy()  # 关闭Tkinter窗口
        run_pygame_game()  # 重新开始游戏

    def quit_game(self):
        self.root.destroy()  # 关闭Tkinter窗口
        exit()  # 退出程序

# 主程序
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    run_pygame_game()  # 运行游戏
    app = GameOverWindow(root)  # 创建游戏结束窗口
    root.deiconify()  # 显示游戏结束窗口
    root.mainloop()  # 进入Tkinter事件循环