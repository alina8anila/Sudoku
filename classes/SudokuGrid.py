from classes.Cell import Cell
import random
class SudokuGrid:
    def __init__(self):
        self.__cell: list[list[int] ]=[[Cell(0, i, j) if 1<=j<=9 and 1<=i<=9 else Cell(-1, i, j) for j in range(11)] for i in range(11)]
        self.__level: int =20

    @property
    def cell(self)->int: return self.__cell
    @property
    def level(self)->int: return self.__level
    @level.setter
    def level(self, new): self.__level=new


    def go_in_all(self, row: int, col: int)->list[int]:
        cells :list[int]=[]
        cells += [self.__cell[row][i] for i in range(1, 10) if i != col]
        cells += [self.__cell[i][col] for i in range(1, 10) if i != row]

        start_row = 1 + 3 * ((row - 1) // 3)
        start_col = 1 + 3 * ((col - 1) // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if i != row or j != col: cells.append(self.__cell[i][j])
        return cells

    def check(self, row: int, col: int, val: int)->bool:
        for i in self.go_in_all(row, col):
            if i.val==val: return bool(0)
        return bool(1)
    
    def set(self, row: int, col: int, val: int):
        list(map(lambda s: self.__cell[s.row][s.col].erase(val), self.go_in_all(row, col))) #for i in self.go_in_all(row, col): self._cell[i.row][i.col].erase(val)
        self.__cell[row][col]=Cell(val, row, col)

    def reset(self, row: int, col: int, val :int):
        self.__cell[row][col]=Cell(0, row, col)
        list(map(lambda s: self.__cell[row][col].erase(s.val), self.go_in_all(row, col))) #for i in self.go_in_all(row, col): self._cell[row][col].erase(i.val)
        for i in self.go_in_all(row, col):
            if self.check(i.row, i.col, val): self.__cell[i.row][i.col].add(val)
            
    def known(self, row :int, col :int)->bool:
        if len(self.__cell[row][col].possible)==1 and self.__cell[row][col].val==0:
            self.set(row, col, next(iter(self.__cell[row][col].possible)))
            return bool(1)
        return bool(0)
    
    def find_empty(self)->list[Cell]:
        empty: list[Cell] =[]
        
        for i in range(1, 10):
            empty+=list(filter(lambda s: s.val==0, self.__cell[i])) #filter
            if len(empty)!=0: break
        return empty
    
    def find_empty_random(self)->Cell:
        empty: list[Cell] =[]
        
        for i in range(1, 10):
            empty+=list(filter(lambda s: s.val==0, self.__cell[i])) #filter
        if len(empty)==0: return
        ind: int=random.randint(0, len(empty)-1)
        return empty[ind]

    def __str__(self)->str:
        ans: str=""
        for i in range(1, 10):
            for j in range(1, 10):
                ans+=str(self.__cell[j][i].val)+" "
            ans+="\n"
        return ans