#!/usr/bin/python3
from SudokuSolver import SudokuSolver
import tkinter as tk
import tkinter.messagebox as mb


class SudokuSolverGUI(object):
    def __init__(self):
        mainWindow = tk.Tk()
        mainWindow.title('SudokuSolver GUI Application')
        mainWindow.geometry('750x400')

        texts = []
        f1 = tk.Frame(mainWindow)
        f1.place(x=20, y=20)
        for i in range(9):
            for j in range(9):
                ent = tk.Entry(f1, text='', width=2,
                               font=('Helvetica', '20', 'bold'))
                texts.append(ent)
                ent.grid(row=i, column=j)

        labels = []
        f2 = tk.Frame(mainWindow)
        f2.place(x=380, y=10)
        for i in range(9):
            for j in range(9):
                lab = tk.Label(f2, text='0', width=2,
                               font=('Helvetica', '20', 'bold'))
                labels.append(lab)
                lab.grid(row=i, column=j)

        def click():
            def new_int(t):
                return int(t) if t else 0
            grid = [list(new_int(t.get()) for t in texts[i*9:i*9+9])
                    for i in range(9)]
            s = SudokuSolver(grid)
            r = s.solve()
            if r.startswith('+'):
                lbs = [list(t for t in labels[i*9:i*9+9]) for i in range(9)]
                for i in range(9):
                    for j in range(9):
                        lbs[i][j].config(text=s.b[i][j])
            else:
                mb.showerror(message=r)

        btn = tk.Button(mainWindow, text='Go!', width=20, command=click)
        btn.place(x=250, y=360)

        mainWindow.mainloop()


if __name__ == "__main__":
    SudokuSolverGUI()
