#!/usr/bin/python3
from SudokuSolver import SudokuSolver
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog


class SudokuSolverGUI(object):
    def __init__(self):
        mainWindow = tk.Tk()
        mainWindow.title('SudokuSolver GUI Application')
        mainWindow.geometry('750x400')

        self.texts = []
        f1 = tk.Frame(mainWindow)
        f1.place(x=20, y=20)
        self.es = []
        for i in range(9):
            for j in range(9):
                self.es.append(tk.StringVar())
                ent = tk.Entry(f1, text='', width=2,
                               font=('Helvetica', '20', 'bold'), textvariable=self.es[i * 9 + j])
                self.texts.append(ent)
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
            grid = [list(new_int(t.get()) for t in self.texts[i * 9 : i * 9 + 9])
                    for i in range(9)]
            s = SudokuSolver(grid)
            r = s.solve()
            if r.startswith('+'):
                lbs = [list(t for t in labels[i * 9 : i * 9 + 9]) for i in range(9)]
                for i in range(9):
                    for j in range(9):
                        lbs[i][j].config(text=s.b[i][j])
            else:
                mb.showerror(message=r)

        def open_file():
            fn = tk.filedialog.askopenfilename(title='选择一个文件', filetypes=[('CSV','*.csv')])
            if fn:
                f = open(fn, 'r', encoding='utf-8')
                txt = f.readlines()
                f.close()
                for i in range(9):
                    for j in range(9):
                        tmp = ''
                        if txt[i].split(',')[j] == '\n':
                            tmp = ''
                        else:
                            tmp = txt[i].split(',')[j]
                        self.es[i * 9 + j].set(tmp)

        go = tk.Button(mainWindow, text='Go!', width=20, command=click)
        go.place(x=250, y=360)

        open_f = tk.Button(mainWindow, text='Open', width=15, command=open_file)
        open_f.place(x=500, y=360)

        mainWindow.mainloop()


if __name__ == "__main__":
    SudokuSolverGUI()
