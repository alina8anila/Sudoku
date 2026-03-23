class Cell:
    def __init__(self, val: int, row: int, col: int):
        self.__val: int =val
        self.__possible: set[int] =set(range(1, 10)) if val==0 else {val}
        self.__row: int =row
        self.__col: int =col

    @property
    def val(self)->int: return self.__val
    @property
    def possible(self)->set: return self.__possible
    @property
    def row(self)->int: return self.__row
    @property
    def col(self)->int: return self.__col

    @val.setter
    def val(self, new: int):
        if new not in range(0, 10): raise ValueError("Value must be in range between 0 and 9") #
        self.__val=new
        if new!=0: self.__possible={new}
        else: self.__possible=set(range(1, 10))
    
    def erase(self, val: int): self.__possible.discard(val)
    def add(self, val: int): self.__possible.add(val)

    def check(self, val: int)-> bool:
        if val in self.__possible: return bool(1)
        return bool(0)


