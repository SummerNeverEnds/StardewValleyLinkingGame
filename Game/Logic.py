from Game.constants import *

class GameLogic:
    def __init__(self, rows, cols, num):
        self.rows = rows
        self.cols = cols
        self.pic_num = num
        self.map = []

    def to_screen(self, x, y):
        return y * PIC_WIDTH + OFFSET_X, x * PIC_HEIGHT + OFFSET_Y

    def generate_map(self):
        total = self.rows * self.cols
        elements = [i % self.pic_num for i in range(total)]
        random.shuffle(elements)
        self.map = [elements[i * self.cols:(i + 1) * self.cols] for i in range(self.rows)]

    def is_link(self, x1, y1, x2, y2):
        if (x1, y1) == (x2, y2):
            return [False, (-1, -1)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if abs(x1 - x2) + abs(y1 - y2) == 1:
            return [
                True,
                [self.to_screen(x1, y1),
                self.to_screen(x2, y2)]
            ]
        path1 = []
        path2 = []
        for dx, dy in dirs:
            x, y = x1 + dx, y1 + dy
            while -1 <= x <= self.rows and -1 <= y <= self.cols:
                if -1 < x < self.rows and -1 < y < self.cols and self.map[x][y] != BLANK:
                    break
                path1.append((x, y))
                x += dx
                y += dy
        for dx, dy in dirs:
            x, y = x2 + dx, y2 + dy
            while -1 <= x <= self.rows and -1 <= y <= self.cols:
                if -1 < x < self.rows and -1 < y < self.cols and self.map[x][y] != BLANK:
                    break
                path2.append((x, y))
                x += dx
                y += dy
        for x, y in path1:
            for i, j in path2:
                if (x == i and x in (-1, self.rows)) or (y == j and y in (-1, self.cols)):
                    return  [
                        True,
                        [self.to_screen(x1, y1),
                        self.to_screen(x, y),
                        self.to_screen(i, j),
                        self.to_screen(x2, y2)]
                    ]
                elif x == i and y != j:
                    if (0 <= x < self.rows and
                            all(0 <= t < self.cols and self.map[x][t] == BLANK for t in range(min(y, j), max(y, j)+1))):
                        return [
                            True,
                            [self.to_screen(x1, y1),
                            self.to_screen(x, y),
                            self.to_screen(i, j),
                            self.to_screen(x2, y2)]
                        ]
                elif y == j and x != i:
                    if (0 <= y < self.cols and
                            all(0 <= t < self.rows and self.map[t][y] == BLANK for t in range(min(x, i), max(x, i)+1))):
                        return [
                            True,
                            [self.to_screen(x1, y1),
                            self.to_screen(x, y),
                            self.to_screen(i, j),
                            self.to_screen(x2, y2)]
                        ]
                elif x == i and y == j:
                    return [
                        True,
                        [self.to_screen(x1, y1),
                         self.to_screen(x, y),
                         self.to_screen(x2, y2)]
                    ]
        return [False, (-1, -1)]

    def clear(self, x1, y1, x2, y2):
        if self.is_link(x1, y1, x2, y2):
            self.map[x1][y1] = BLANK
            self.map[x2][y2] = BLANK
            return True
        return False

    def is_blank(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.map[x][y] != BLANK:
                    return False
        return True

    def search_path(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.map[x][y] == BLANK:
                    continue
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.map[i][j]==BLANK or (i == x and j == y):
                            continue
                        result = self.is_link(x, y, i, j)
                        if result[0] and self.map[x][y] == self.map[i][j]:
                            return result
        return [False, (-1, -1)]

    def reset(self):
        remaining = []
        for x in range(self.rows):
            for y in range(self.cols):
                if self.map[x][y] != BLANK:
                    remaining.append(self.map[x][y])
        random.shuffle(remaining)
        idx = 0
        for x in range(self.rows):
            for y in range(self.cols):
                if self.map[x][y] != BLANK:
                    self.map[x][y] = remaining[idx]
                    idx += 1
