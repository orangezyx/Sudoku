import curses
import random
from random import shuffle, randrange


class SudokuGame(object):
    def __init__(self):
        self.game_frm = curses.newwin(curses.LINES - 1, curses.COLS - 1, 0, 0)
        self.cols = curses.COLS
        self.game_frm.addstr(
            5, 0, '+---Choose the difficult---+'.center(self.cols, ' '))
        self.game_frm.addstr(
            6, 0, '|         1. Easy          |'.center(self.cols, ' '))
        self.game_frm.addstr(
            7, 0, '|         2. Normal        |'.center(self.cols, ' '))
        self.game_frm.addstr(
            8, 0, '|         3. Hard          |'.center(self.cols, ' '))
        self.game_frm.addstr(
            9, 0, '|         4. Expert        |'.center(self.cols, ' '))
        self.game_frm.addstr(
            10, 0, '|         q. Exit          |'.center(self.cols, ' '))
        self.game_frm.addstr(
            11, 0, '+--------------------------+'.center(self.cols, ' '))
        self.game_frm.refresh()
        while True:
            diff = self.game_frm.getch()
            if diff == ord('q'):
                break
            elif diff in [ord('1'), ord('2'), ord('3'), ord('4')]:
                self.game_loop(diff - 48)  # diff 是ascii码 所以要减48
                break
        self.game_frm.clear()
        self.game_frm.refresh()

    '''
    1. 简单难度 38-42个格子
    2. 普通难度 32-37个格子
    3. 困难难度 25-31个格子
    4. 专家难度 20-24个格子
    '''

    def game_loop(self, diff):
        n = 0
        if diff == 1:
            n = random.randint(38, 42)
        elif diff == 2:
            n = random.randint(32, 37)
        elif diff == 3:
            n = random.randint(25, 31)
        elif diff == 4:
            n = random.randint(20, 24)

        self.board = BoarkGenerator.generate(self, n)  # 生成带几个数字的 board

        base_ui = '+-------+-------+-------+\n'
        i = 0
        for j in self.board:
            i += 1
            base_ui += f'| {j[0]} {j[1]} {j[2]} | {j[3]} {j[4]} {j[5]} | {j[6]} {j[7]} {j[8]} |\n'
            if i == 3 or i == 6:
                base_ui += '+-------+-------+-------+\n'
        base_ui += '+-------+-------+-------+\n'

        base_ui = base_ui.split('\n')

        notify_text_1 = '[1-9] put the num     [q] quit'
        notify_text_2 = '[r] restart           [s] save'

        for r in range(len(base_ui)):
            self.game_frm.addstr(5 + r, 0, base_ui[r].center(curses.COLS))
        self.game_frm.addstr(5 + len(base_ui) + 1, 0,
                             notify_text_1.center(curses.COLS))
        self.game_frm.addstr(5 + len(base_ui) + 2, 0,
                             notify_text_2.center(curses.COLS))
        self.game_frm.getch()


class BoarkGenerator(object):
    def generate(self, clean_nums):  # 生成数独
        # 初始网格
        result = []
        line = list(range(1, 10))
        for i in range(9):
            result.append(line)
            line.append(line.pop(0))
            line = line[:]

        def switchRows(first, second):
            (result[first],
             result[second]) =\
                (result[second],
                 result[first])

        def switchColumns(first, second):
            for index in range(9):
                (result[index][first],
                 result[index][second]) =\
                    (result[index][second],
                     result[index][first])

        # 随机交换行
        randomRows = list(range(9))
        shuffle(randomRows)
        for i in range(0, 7, 2):
            switchRows(randomRows[i],
                       randomRows[i + 1])
        # 随机交换列
        randomColumns = list(range(9))
        shuffle(randomColumns)
        for i in range(0, 7, 2):
            switchColumns(randomColumns[i],
                          randomColumns[i + 1])
        # 随机清空格子
        positions = {(x % 9, int(x / 9))
                     for x in random.sample(range(0, 81), 81 - clean_nums)}
        for row, col in positions:
            result[row][col] = ' '

        return result
