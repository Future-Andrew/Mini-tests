import random
import curses

# 游戏设置
WIDTH, HEIGHT = 40, 40
MINES = 20

# 初始化地雷位置
mines = set()
while len(mines) < MINES:
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    mines.add((x, y))

# 游戏状态
board = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
flags = set()

def is_mine(x, y):
    return (x, y) in mines

def is_flagged(x, y):
    return (x, y) in flags

def toggle_flag(stdscr, x, y):
    if is_flagged(x, y):
        flags.remove((x, y))
    else:
        flags.add((x, y))
    draw_board(stdscr)

def draw_board(stdscr):
    stdscr.clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if is_flagged(x, y):
                stdscr.addstr(y, x*2, 'F', curses.color_pair(1))  # 绿色
            elif is_mine(x, y):
                stdscr.addstr(y, x*2, 'X', curses.color_pair(2))  # 红色
            else:
                stdscr.addstr(y, x*2, ' ', curses.color_pair(0))  # 白色
    stdscr.refresh()

def main(stdscr):
    # 初始化颜色
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # 旗子
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # 地雷

    draw_board(stdscr)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT or key == curses.KEY_RIGHT or key == curses.KEY_UP or key == curses.KEY_DOWN:
            x, y = stdscr.getmaxyx()[1] // 2, stdscr.getmaxyx()[0] // 2
            if key == curses.KEY_LEFT:
                x -= 1
            elif key == curses.KEY_RIGHT:
                x += 1
            elif key == curses.KEY_UP:
                y -= 1
            elif key == curses.KEY_DOWN:
                y += 1
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                if key == ord('f'):  # 按下 'f' 来标记旗子
                    toggle_flag(stdscr, x, y)
                else:
                    # 这里可以添加打开格子的逻辑
                    pass

curses.wrapper(main)