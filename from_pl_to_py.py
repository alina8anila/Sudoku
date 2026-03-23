from pyswip import Prolog
import os
from classes.SudokuGrid import SudokuGrid

prolog = Prolog()
path = os.path.join(os.path.dirname(__file__), "check.pl")
prolog.consult(path)

def can_place_prolog(grid : SudokuGrid, row, col, val):

    rows=[]
    for i in range(1, 10):
        ro=[]
        for j in range(1, 10):
            ro.append(grid.cell[i][j].val)
        rows.append(ro)
    
    query="Rows=["
    for i in range(9):
        if not i==0: query+=',' 
        query+="["
        for j in range(9):
            query+=str(rows[i][j])
            if not j==8: query+=','
        query+="]"
    query+=f"],can_place(Rows, {row}, {col}, {val})."

    #print(query)
    
    for i in prolog.query(query): return True
    return False