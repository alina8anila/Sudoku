import tkinter as tk
from classes.Generator import Generator
import copy
from export_to_pdf import export_pdf

def you_lose_window(root, fill_again):
    lose = tk.Toplevel(root)
    lose.title("Game Over")
    lose.geometry("800x400")

    tk.Label(lose, text="YOU LOSE 💔", font=("Arial", 60), fg="red").pack(pady=10)
    tk.Button(lose, text="Try again", font=("Arial", 40), command=lambda: (lose.destroy(), fill_again())).pack(pady=20)

def you_win_window(root, fill_again):
    win = tk.Toplevel(root)
    win.title("Congratulations")
    win.geometry("800x400")

    tk.Label(win, text="YOU WIN 🎉", font=("Arial", 60), fg="green").pack(pady=10)
    tk.Button(win, text="Play again", font=("Arial", 40), command=lambda: (win.destroy(), fill_again())).pack(pady=20)


def main_window():
    root = tk.Tk()
    root.title("sudoku")
    root.geometry("1200x750")

    c=tk.Canvas(root, width=1200, height=750)
    c.pack()

    heart: int=0
    cell: int =75
    start: int =10
    gap: int =3
    gridv: list[list[tk.StringVar]]=[[tk.StringVar() for _ in range(10)] for _ in range(10)]
    highlighted: list = []
    grid=Generator()
    note: tk.BooleanVar=tk.BooleanVar()

    tk.Checkbutton(text="note", variable=note, onvalue=1, offvalue=0, font=("Aria", 40)).place(x=750, y=380)
    heart1=tk.Label(root, text="❤️", font=("Aria", 50))
    heart2=tk.Label(root, text="❤️", font=("Aria", 50))
    heart3=tk.Label(root, text="❤️", font=("Aria", 50))
    heart1.place(x=830, y=50)
    heart2.place(x=900, y=50)
    heart3.place(x=970, y=50)

    def minus_heart():
        nonlocal heart
        heart+=1
        if heart==1: heart1["text"]="💔"
        if heart==2: heart2["text"]="💔"
        if heart==3: 
            heart1["text"]="❤️"
            heart2["text"]="❤️"
            you_lose_window(root, fill_again)

    def on_change(row: int, col: int):
        nonlocal note
        if note.get():
            return
        val: int= gridv[row][col].get()
        if val=="":
            grid.reset(row, col, grid.cell[row][col].val)
            return

        if val not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            minus_heart()
            gridv[row][col].set("")
            return
        if not grid.check(row, col, int(val)):
            minus_heart()
            gridv[row][col].set("")
            return
        
        full=copy.deepcopy(grid)
        full.set(row, col, int(gridv[row][col].get()))
        if not full.constraint_satisfaction_prolog():
            minus_heart()
            gridv[row][col].set("")
            return
        grid.set(row, col, int(gridv[row][col].get()))
        if len(grid.find_empty())==0: you_win_window(root, fill_again)

    def printgrid():
        clear_highlight()
        for i in range(1, 10):
            for j in range(1, 10):
                if grid.cell[i][j].val == 0:
                    gridv[i][j] = tk.StringVar()
                    gridv[i][j].trace_add("write", lambda *args, a=i, b=j: on_change(a, b))
                    e=tk.Entry(root, textvariable=gridv[i][j], width=2, font=("Arial", 60))
                else: 
                    e = tk.Label(root, text=grid.cell[i][j].val, width=1, font=("Arial", 60))
                c.create_window(start+(i-1)*(gap+cell), start+(j-1)*(cell+gap), window=e, width=cell, height=cell, anchor="nw")

    def clear_highlight():
        for i in highlighted:
            c.itemconfig(i, outline="")
        highlighted.clear()

    def highlight_number(num):
        clear_highlight()
        for i in range(1, 10):
            for j in range(1, 10):
                if grid.cell[i][j].val==num:
                    rect=c.create_rectangle(start+(i-1)*(gap+cell), start+(j-1)*(cell+gap), start+i*(gap+cell)-gap, start+j*(cell+gap)-gap, outline="red", width=8)
                    highlighted.append(rect)


    level=tk.IntVar(value=10)

    def fill_again():
        nonlocal grid, heart
        heart=0
        heart1["text"]="❤️"
        heart2["text"]="❤️"
        grid.clean()
        grid.fill_all()
        grid.removesome()
        printgrid()

    def make_hint():
        empty=grid.find_empty_random()
        full=copy.deepcopy(grid)
        full.fill_all()
        grid.set(empty.row, empty.col, full.cell[empty.row][empty.col].val)
        printgrid()
        if len(grid.find_empty())==0: you_win_window(root, fill_again)

    def func_set_level():
        grid.level=level.get()
        fill_again()

    fill_again()

    for i in range(10):
        if i%3!=0:
            co: str="grey"
            w: int=2
        else:
            co: str="white"
            w: int=5
        c.create_line(start+i*(cell+gap), start, start+i*(cell+gap), start+9*(cell+gap), fill=co, width=w)
        c.create_line(start, start+i*(cell+gap), start+9*(cell+gap), start+i*(cell+gap), fill=co, width=w)

    for i in range(1, 6): 
        rad=tk.Radiobutton(root, text=f"level{str(i)}", variable=level, value=i*10, command=func_set_level)
        rad.place(x=1100, y=200+i*50)

    again=tk.Button(root, text="New game", command=fill_again, width=7, height=1, font=("Aria", 50))
    again.place(x=800, y=500)
    save_pdf=tk.Button(root, text="Save in pdf", command=lambda: export_pdf(grid), width=7, height=1, font=("Aria", 30))
    save_pdf.place(x=850, y=600)

    hint=tk.Button(text="Hint", command=make_hint, width=4, height=3, font=("Aria", 25), background="lightyellow")
    hint.place(x=875, y=350)

    
    for n in range(1, 10):
        btn = tk.Button(root, text=str(n), font=("Arial", 30), width=2, command=lambda v=n: highlight_number(v))
        btn.place(x=820+(n-1)%3*70, y=150+(n-1)//3*45)


    
    root.mainloop()

main_window()