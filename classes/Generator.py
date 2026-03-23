from classes.Solver import Solver
import random


class Generator(Solver):
    
    def fill_random(self):
        temp: list[int] =list(range(1, 10))
        random.shuffle(temp)
        for i in range(1, 10): self.set(1, i, temp[i-1])

        temp.pop()
        random.shuffle(temp)
        for i in range(2, 10): self.set(i, 9, temp[i-2])

    def fill_all(self):
        self.constraint_satisfaction_prolog()#self.constraint_satisfaction()

    def clean(self):
        for i in range(1, 10):
            for j in range(1, 10):
                self.cell[i][j].val=0

    def removesome(self):
        st: set[tuple[int, int]]=set()
        for i in range(self.level):
            x: int =random.randint(1, 9)
            y: int =random.randint(1, 9)
            while (x, y) in st:
                x: int =random.randint(1, 9)
                y: int =random.randint(1, 9)
            st.add((x, y))

            self.reset(y, x, self.cell[x][y].val)