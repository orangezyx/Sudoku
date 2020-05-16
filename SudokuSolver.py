#!/usr/bin/python3
import datetime
import sys


class Sudoku(object):
    def __init__(self, board):
        self.b = board
        self.t = 0

    def get_next(self, x, y):  # 得到下一个未填项
        for next_solution in range(y + 1, 9):
            if self.b[x][next_solution] == 0:
                return x, next_solution
        for row_n in range(x + 1, 9):
            for col_n in range(0, 9):
                if self.b[row_n][col_n] == 0:
                    return row_n, col_n
        return -1, -1  # 若无下一个未填项，返回-1

    block_in_grid = {(x, y): (x // 3) * 3 + (y // 3) for x in range(9) for y in range(9)}
    grid_get_block = {x: [] for x in range(9)}

    for i, j in block_in_grid.items():
        grid_get_block[j].append(i)

    def possible_num(self, x, y):  # 获得一个格子可能的数字集合
        whole = set(range(1, 10))
        x_set = set(self.b[x])
        y_set = {self.b[i][y] for i in range(9)}
        block_num = self.block_in_grid[(x, y)]
        block_set = {self.b[i][j] for i, j in self.grid_get_block[block_num]}
        return whole - x_set - y_set - block_set

    def try_it(self, x, y):  # 主循环
        if self.b[x][y] == 0:
            possible = self.possible_num(x, y)
            for i in possible:  # 从可能的数字中尝试
                self.t += 1
                self.b[x][y] = i  # 将可能的数字填入0格
                next_x, next_y = self.get_next(x, y)  # 得到下一个0格
                if next_x == -1:  # 如果无下一个0格
                    return True  # 返回True
                else:  # 如果有下一个0格，递归判断下一个0格直到填满数独
                    end = self.try_it(next_x, next_y)
                    if not end:  # 在递归过程中存在不符合条件的，即 使try_it函数返回None的项
                        self.b[x][y] = 0  # 回朔到上一层继续
                    else:
                        return True

    def check_is_legal(self):
        # 判断每一行是否有效
        for i in range(9):
            for j in self.b[i]:
                if (j not in range(0, 10)) or (self.b[i].count(j) > 1 and j != 0):
                    return False, 'There are %d same number %d in line %d.' % (self.b[i].count(j), j, (i + 1))
        # 判断每一列是否有效
        columns = [[r[col] for r in self.b] for col in range(len(self.b[0]))]
        for i in range(9):
            for j in columns[i]:
                if (j not in range(0, 10)) or (columns[i].count(j) > 1 and j != 0):
                    return False, 'There are %d same number %d in column %d.' % (self.b[i].count(j), j, (i + 1))
        # 判断九宫格是否有效
        for i in range(3):
            for j in range(3):
                grid = [tem[j * 3:(j + 1) * 3] for tem in self.b[i * 3:(i + 1) * 3]]
                merge_str = grid[0] + grid[1] + grid[2]  # 合并为一个list[]
                for m in merge_str:
                    if (m not in range(0, 10)) or (merge_str.count(m) > 1 and m != 0):
                        return False, 'There are %d same number %d in block %d.' \
                               % (merge_str.count(m), m, (3 * i + j + 1))
        return True, 'OK'
    

    def solve(self):
        s = ''
        legal, error_s = self.check_is_legal()
        if not legal:
            s += "Error: The sudoku is illegal!\n" + error_s
            return s

        begin = datetime.datetime.now()
        if self.b[0][0] == 0:
            self.try_it(0, 0)  # 如果第一格为空，则从此开始尝试
        else:
            x, y = self.get_next(0, 0)  # 否则就获得从第一个格子的下一个空格子开始
            self.try_it(x, y)
        end = datetime.datetime.now()

        for i in self.b:
            for j in i:
                if j == 0:
                    s = 'Failure to solve, the given Sudoku is unsolved or the Sudoku is given incorrectly.'
                    return s
        
        s += '+-------+-------+-------+\n'
        i = 0
        for j in self.b:
            i += 1
            s += f'| {j[0]} {j[1]} {j[2]} | {j[3]} {j[4]} {j[5]} | {j[6]} {j[7]} {j[8]} |\n'
            if i == 3 or i == 6:
                s += '+-------+-------+-------+\n'
        s += '+-------+-------+-------+\n'
        s += 'Total cost time: ' + str((end - begin))
        s += '\nTry times: ' + str(self.t)
        return s


usage = '''Usage: Sudoku.py <FILE>\n      -h, --help        Print this help'''

def main(argv):
    lines = None
    if len(argv) != 2:
        print(usage)
        return
    f = None
    if argv[1] in ('-h', '--help'):
        print(usage)
        return
    try:
        f = open(argv[1], 'r', encoding='utf-8')
    except IOError:
        print('Error: File do not exists!')
        return

    FormatErrorMessage = 'Error: Sudoku format error, type -h or --help for more.'
    lines = f.read().splitlines()
    if len(lines) != 9:
        print(FormatErrorMessage + "\nLine count error, request 9 lines, found %d lines." % len(lines))
        return
    for i in range(9):
        if lines[i].count(',') != 8:
            print(FormatErrorMessage + ("\nComma count error, request 8 commas per line, found %d commas in line %d." % (lines[i].count(','), i + 1)))
            return

    grid = map(lambda i: i.split(","), lines)

    def new_int(t):
        return int(t) if t else 0

    grid = [list(map(new_int, i)) for i in grid]

    s = Sudoku(grid)
    print(s.solve())

if __name__ == '__main__':
    main(sys.argv)
