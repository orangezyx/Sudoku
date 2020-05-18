#!/usr/bin/python3
import tkinter as tk
import tkinter.messagebox as mb
import SudokuGame


class SudokuGameGUI(object):
    def __init__(self):
        mainWindow = tk.Tk()
        mainWindow.title('SudokuGame GUI Application')
        mainWindow.geometry('400x400')

        texts = []
        f1 = tk.Frame(mainWindow)
        f1.place(x=20, y=20)

        self.board = SudokuGame.BoardGenerator.generate(self, 40)
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ' ':
                    ent = tk.Entry(f1, text='', width=2,
                               font=('Helvetica', '20', 'bold'))
                    texts.append(ent)
                    ent.grid(row=i, column=j)
                else:
                    lab = tk.Label(f1, text=str(self.board[i][j]), width=2,
                               font=('Helvetica', '20', 'bold'))
                    texts.append(lab)
                    lab.grid(row=i, column=j)

        mainWindow.mainloop()


if __name__ == "__main__":
    SudokuGameGUI()
