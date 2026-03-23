from classes.SudokuGrid import SudokuGrid
import random
from from_pl_to_py import can_place_prolog

class Solver(SudokuGrid):
    
    def constraint_propagation(self):
        change: bool =1
        while change:
            change: bool =0
            for i in range(1, 10):
                for j in range(1, 10):
                    if self.known(i, j): change: bool =1

    def constraint_satisfaction(self):
        new: int =self.find_empty()
        if len(new)==0: return 1
        row: int =new[0].row
        col: int =new[0].col

        candidats: list[int]=list(self.cell[row][col].possible)
        random.shuffle(candidats)
        if len(candidats)==0: return 0
    
        for val in candidats:
            self.set(row, col, val)
            x: int =self.constraint_satisfaction()
            if x!=0: return 1
            self.reset(row, col, val)
        return 0
    
    def constraint_satisfaction_prolog(self):
        new=self.find_empty()
        if len(new)==0: return 1
        row: int =new[0].row
        col: int =new[0].col

        candidats: list[int] =list(range(1, 10))
        random.shuffle(candidats)
        for val in candidats:
            if not can_place_prolog(self, row, col, val): continue
            self.set(row, col, val)
            x: int =self.constraint_satisfaction_prolog()
            if x!=0: return 1
            self.reset(row, col, val)
        return 0