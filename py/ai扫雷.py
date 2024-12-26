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

    def dfs(self, cnt, edges, n, i, s, cur, sum_, mineMin, mineMax, mineCnt, perBoardCnt, allStatus, saveAllStatus):
        if sum_ == self.SUMLIMIT:
            self.flag = False
            return
        if mineMax < 0 or mineMin > (n - i):
            return
        for j in range(len(cnt)):
            if cnt[j][0] < 0 or cnt[j][1][0] + cnt[j][1][1] < cnt[j][0]:
                return
        if i == n:
            sum_ += 1
            mineCur = sum(cur)
            mineCnt[mineCur] = mineCnt.get(mineCur, 0) + 1
            for idx in range(len(s)):
                if cur[idx]:
                    perBoardCnt[idx][mineCur] = perBoardCnt[idx].get(mineCur, 0) + 1
            if saveAllStatus:
                allStatus.append(cur.copy())
                for idx in range(len(allStatus[-1])):
                    if allStatus[-1][idx] == 1:
                        allStatus[-1][idx] = -2
            return

        for j in edges[i]:
            cnt[j][1][0] -= 1
        cur[i] = 0
        self.dfs(cnt, edges, n, i + 1, s, cur, sum_, mineMin, mineMax, mineCnt, perBoardCnt, allStatus, saveAllStatus)

        for j in edges[i]:
            cnt[j][1][0] += 1
        cur[i] = 1
        for j in edges[i]:
            cnt[j][0] -= 1
            cnt[j][1][0] -= 1
        self.dfs(cnt, edges, n, i + 1, s, cur, sum_, mineMin - 1, mineMax - 1, mineCnt, perBoardCnt, allStatus, saveAllStatus)
        cur[i] = 0
        for j in edges[i]:
            cnt[j][0] += 1
            cnt[j][1][0] += 1

    def dfs_detect(self, board, points, safeCells, unknownCells, prob, mineMin, mineMax, mineCnt, perBoardCnt, allStatus, saveAllStatus):
        unknownSet = set(unknownCells)
        cnt = []
        edges = []
        
        for safeCell in safeCells:
            it = safeCell
            cnt.append([board[it[0]][it[1]], [0, 0]])
            for ii in range(max(0, it[0] - 1), min(self.n, it[0] + 2)):
                for jj in range(max(0, it[1] - 1), min(self.m, it[1] + 2)):
                    cnt[-1][0] -= (board[ii][jj] == -2)
                    if board[ii][jj] == -1:
                        if (ii, jj) not in unknownSet:
                            cnt[-1][1][1] += 1
                        else:
                            cnt[-1][1][0] += 1

        for unknownCell in unknownCells:
            edges.append([])
            for j, safeCell in enumerate(safeCells):
                if abs(safeCell[0] - unknownCell[0]) <= 1 and abs(safeCell[1] - unknownCell[1]) <= 1:
                    edges[-1].append(j)

        cells = len(unknownCells)
        sum_ = 0
        s = [0] * cells
        cur = [0] * cells
        mineCnt.clear()
        perBoardCnt.clear()
        perBoardCnt = [{} for _ in range(cells)]
        self.dfs(cnt, edges, cells, 0, s, cur, sum_, mineMin, mineMax, mineCnt, perBoardCnt, allStatus, saveAllStatus)

        for i in range(cells):
            if s[i] == 0:
                points.append(unknownCells[i])
            elif s[i] == sum_:
                board[unknownCells[i][0]][unknownCells[i][1]] = -2
            else:
                prob[unknownCells[i][0]][unknownCells[i][1]] = s[i] / sum_

        if saveAllStatus:
            for curStatus in allStatus:
                for j in range(len(curStatus)):
                    if curStatus[j] == 0:
                        for ii in range(max(0, unknownCells[j][0] - 1), min(self.n, unknownCells[j][0] + 2)):
                            for jj in range(max(0, unknownCells[j][1] - 1), min(self.m, unknownCells[j][1] + 2)):
                                curStatus[j] += (board[ii][jj] == -2)
                        for k in range(len(curStatus)):
                            curStatus[j] += (curStatus[k] == -2 and
                                             abs(unknownCells[j][0] - unknownCells[k][0]) <= 1 and
                                             abs(unknownCells[j][1] - unknownCells[k][1]) <= 1)

    def floodfill(self, board, use, safeCells, unknownCells, i, j):
        use.add((i, j))
        if board[i][j] == -1:
            unknownCells.append((i, j))
        else:
            safeCells.append((i, j))
        for ii in range(max(0, i - 1), min(self.n, i + 2)):
            for jj in range(max(0, j - 1), min(self.m, j + 2)):
                if board[ii][jj] != -2 and (ii, jj) not in use and (board[ii][jj] * board[i][j] < 0):
                    self.floodfill(board, use, safeCells, unknownCells, ii, jj)

    def status_split(self, allStatus, ids, idsList):
        if not ids:
            return
        for i in range(len(allStatus[0])):
            allSame = True
            noMine = True
            for id_ in ids:
                allSame &= (allStatus[id_][i] == allStatus[ids[0]][i])
                noMine &= (allStatus[id_][i] >= 0)
            if noMine and not allSame:
                idsDict = {}
                for id_ in ids:
                    idsDict.setdefault(allStatus[id_][i], []).append(id_)
                for spids in idsDict.values():
                    self.status_split(allStatus, spids, idsList)
                return
        idsList.append(ids)

    def deep_dfs(self, allStatus, ids, prob, f):
        if tuple(ids) in f:
            return f[tuple(ids)]
        if len(ids) == 1:
            for sel in range(len(prob)):
                prob[sel] = (allStatus[ids[0]][sel] < 0)
            return f[tuple(ids)] , 1.0

        ret = 0.0
        order = []
        for sel in range(len(prob)):
            mine = sum(allStatus[i][sel] < 0 for i in ids)
            order.append((mine, sel))

        for it in order:
            sel = it[1]
            idsList = []
            cur = []
            for i in ids:
                if allStatus[i][sel] >= 0:
                    cur.append(i)
            