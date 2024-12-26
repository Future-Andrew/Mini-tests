import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('自动扫雷')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定义游戏参数
grid_size = 10
mine_count = 20
revealed = set()

# 生成网格
def generate_grid():
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    mines = set()
    while len(mines) < mine_count:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        if (x, y) not in mines:
            mines.add((x, y))
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) != (x, y):
                        grid[nx][ny] += 1
    return grid, mines

grid, mines = generate_grid()

# 绘制网格
def draw_grid():
    for x in range(grid_size):
        for y in range(grid_size):
            color = WHITE if (x, y) not in revealed else GREEN if grid[x][y] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * 60, y * 60, 60, 60), 0 if (x, y) in mines else 1)
            if grid[x][y] > 0 and (x, y) in revealed:
                font = pygame.font.Font(None, 36)
                text = font.render(str(grid[x][y]), True, BLACK)
                screen.blit(text, (x * 60 + 30 - text.get_width() // 2, y * 60 + 30 - text.get_height() // 2))

# 检查是否胜利
def check_win():
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] > 0 and (x, y) not in revealed:
                return False
    return True

# 自动扫雷逻辑
def auto_reveal():
    for x in range(grid_size):
        for y in range(grid_size):
            if (x, y) not in revealed and grid[x][y] == 0:
                revealed.add((x, y))
                auto_reveal()

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            x, y = mouse_x // 60, mouse_y // 60
            if event.button == 1:  # 左键点击
                if (x, y) not in revealed:
                    revealed.add((x, y))
                    if (x, y) in mines:
                        running = False
                    elif grid[x][y] == 0:
                        auto_reveal()
            elif event.button == 3:  # 右键点击
                if (x, y) not in revealed:
                    revealed.add((x, y))
    
    screen.fill(GRAY)
    draw_grid()
    
    if check_win():
        font = pygame.font.Font(None, 36)
        text = font.render('恭喜，你赢了！', True, GREEN)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    
    pygame.display.flip()

pygame.quit()
sys.exit()