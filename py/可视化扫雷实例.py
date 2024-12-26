import matplotlib.pyplot as plt
import matplotlib.patches as patches

class MineSolver:
    def __init__(self, n, m, mine):
        self.SUMLIMIT = 10000000
        self.DEEPDFSLIMIT = 1000
        self.n = n
        self.m = m
        self.mine = mine
        self.mineProb = [[0.0] * (mine + 2) for _ in range(n * m + 1)]
        self.mineProb[0][0] = 1.0
        
        for i in range(n * m):
            for j in range(mine + 1):
                self.mineProb[i + 1][j] += self.mineProb[i][j]
                if j + 1 <= mine:
                    self.mineProb[i + 1][j + 1] += self.mineProb[i][j]

    def simple_detect(self, board):
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] > 0:
                    s = 0
                    for ii in range(max(0, i - 1), min(self.n, i + 2)):
                        for jj in range(max(0, j - 1), min(self.m, j + 2)):
                            s += (board[ii][jj] < 0)
                    if s == board[i][j]:
                        for ii in range(max(0, i - 1), min(self.n, i + 2)):
                            for jj in range(max(0, j - 1), min(self.m, j + 2)):
                                if board[ii][jj] == -1:
                                    board[ii][jj] = 0

    def visualize_board(self, board):
        fig, ax = plt.subplots()
        ax.set_title('Mine Sweeper Game')
        for i in range(self.n):
            for j in range(self.m):
                color = 'gray' if board[i][j] == -1 else 'white'
                if board[i][j] == -2:
                    color = 'black'
                elif board[i][j] > 0:
                    color = 'blue'
                    text = str(board[i][j])
                else:
                    text = ''
                rect = patches.Rectangle((j, i), 1, 1, linewidth=1, edgecolor='r', facecolor=color)
                ax.add_patch(rect)
                if text:
                    ax.text(j + 0.5, i + 0.5, text, ha='center', va='center', color='white')
        plt.axis('off')
        plt.show()

# 创建 MineSolver 实例
n = 10  # 行数
m = 10  # 列数
mine = 20  # 地雷数量
solver = MineSolver(n, m, mine)

# 初始化棋盘
board = [[-1 for _ in range(m)] for _ in range(n)]  # 所有格子初始化为未知

# 假设我们在 (0, 0) 位置发现了一个数字 2
board[0][0] = 2

# 调用 simple_detect 方法
solver.simple_detect(board)

# 可视化棋盘
solver.visualize_board(board)