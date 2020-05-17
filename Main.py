#!/usr/bin/python3
import curses
import os
import SudokuGame
import SudokuGameGUI
import SudokuSolverGUI
import LeaderBoard

main_form = curses.initscr()
curses.curs_set(0)


def display_info(x, y, str, attr=0):
    if attr == 1:  # 是否以颜色显示
        main_form.addstr(y, x, str, curses.color_pair(1))
    else:
        main_form.addstr(y, x, str)
    main_form.refresh()


def set_win():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, -1)
    curses.noecho()
    curses.cbreak()
    main_form.keypad(True)


def unset_win():
    curses.nocbreak()
    main_form.keypad(True)
    curses.echo()
    curses.endwin()


def print_main_menu():
    hello_txt = '''   _____           __      __        
  / ___/__  ______/ /___  / /____  __
  \__ \/ / / / __  / __ \/ //_/ / / /
___/ / /_/ / /_/ / /_/ / ,< / /_/ / 
/____/\__,_/\__,_/\____/_/|_|\__,_/  
'''

    game_menu = '''Game Start With Console

Game Start With GUI (issue)

Solve A Game (issue)

LeaderBoard

Exit'''
    hello_txt = hello_txt.split('\n')
    game_menu = game_menu.split('\n')

    columns, lines = os.get_terminal_size()

    t = 0

    for i in range(int((lines - len(hello_txt) - len(game_menu)) / 2)):
        display_info(0, t, '\n')
        t += 1

    for l in range(len(hello_txt)):
        display_info(0, t, str.center(hello_txt[l], columns, ' '))
        t += 1

    for j in range(len(game_menu)):
        if j in [0, 2, 4, 6, 8] and j == currentline:
            display_info(0, t, str.center(
                '-> ' + game_menu[j], columns, ' '), 1)
        else:
            display_info(0, t, str.center(game_menu[j], columns, ' '))
        t += 1


currentline = 0


def main_menu_loop():
    global currentline
    while True:
        c = main_form.getch()
        if c == curses.KEY_DOWN:
            if currentline == 8:
                currentline = 0
                print_main_menu()
            else:
                currentline += 2
                print_main_menu()
        elif c == curses.KEY_UP:
            if currentline == 0:
                currentline = 8
                print_main_menu()
            else:
                currentline -= 2
                print_main_menu()
        elif c == curses.KEY_ENTER or c == 10 or c == 13:
            if currentline == 0:  # Console game
                console_game()
            elif currentline == 2:  # GUI Game
                # gui_game() # With issue while launch the GUI App.
                break
            elif currentline == 4:  # Solve
                # gui_solver() # With issue while launch the GUI App.
                break
            elif currentline == 6:  # LeaderBoard
                leader_board()
            elif currentline == 8:  # Exit
                break


def console_game():
    game = SudokuGame.SudokuGame()
    print_main_menu()


def gui_game():
    game = SudokuGameGUI.SudokuGameGUI()


def gui_solver():
    solver = SudokuSolverGUI.SudokuSolverGUI()


def leader_board():
    leaders = LeaderBoard.LeaderBoard()
    print_main_menu()


def main():
    set_win()
    print_main_menu()
    main_menu_loop()
    unset_win()


if __name__ == '__main__':
    main()
