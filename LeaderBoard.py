#!/usr/bin/python3
import curses
import sqlite3


class LeaderBoard(object):
    def __init__(self):
        self.leaders = curses.newwin(curses.LINES - 1, curses.COLS - 1, 0, 0)
        self.cols = curses.COLS
        self.leaders.addstr(
            5, 0, '+------------------------Current Leader Border------------------------+'.center(self.cols, ' '))

        conn = sqlite3.connect('leaders.db')
        cursor = conn.cursor()

        sql = 'select * from Games order by GameTime'
        cursor.execute(sql)

        values = cursor.fetchall()
        cursor.close()
        conn.close()
        self.leaders.addstr(
            7, int((self.cols - 67) / 2) + 1, 'Order\tName\tDifficulty\tDate\t\t\tTime')
        t = 0
        for i in values:
            t += 1
            diff = ('Easy', 'Normal', 'Hard', 'Expert')[int(i[4])]
            self.leaders.addstr(
                7 + t, int((self.cols - 67) / 2) + 1, f'{t}\t\t{i[1]}\t{diff}\t\t{i[3]}\t{i[2]}')
        self.leaders.addstr(
            7 + t + 2, 0, '+---------------------------------------------------------------------+'.center(self.cols, ' '))
        self.leaders.addstr(
            7 + t + 4, 0, '[Anykey] Quit'.center(self.cols, ' '))
        self.leaders.refresh()
        self.leaders.getch()
