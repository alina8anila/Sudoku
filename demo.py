from classes.Generator import Generator
from from_pl_to_py import can_place_prolog


gen=Generator()
gen.fill_random()
print(gen)
print(can_place_prolog(gen, 2, 2, 5))
#gen.fill_all()
print(gen)
for i in gen.find_empty(): print(i.row, i.col)

"""
grid=SudokuGrid()
print(grid)
grid.set(2, 2, 1)
print(grid)

print("possible in 4, 6:", grid.cell[4][6].possible)
print("possible in 2, 2:", grid.cell[2][2].possible)

print(grid.cell[2][2].check(2))
print(grid.cell[2][2].check(1))

print("cell 2 2:", list(dict.fromkeys(gen.cell[2][2].possible)), '\n')

solver=Solver()
solver.set(1, 1, 1)
solver.set(1, 2, 2)
solver.set(1, 3, 3)
solver.set(2, 1, 9)
solver.set(2, 2, 5)
solver.set(2, 3, 6)
solver.set(3, 1, 7)
solver.set(3, 2, 8)

print(solver)
solver.constraint_propagation()
print(solver)
print("empty:", solver.find_empty()[0].row, solver.find_empty()[0].col)
solver.constraint_satisfaction()
print(solver)


generator2=Generator()
generator2.fill_all()
print("generator2")
print(generator2)


generator1=Generator()
generator1.fill_all()
generator1.removesome()
print("generator1")
print(generator1)
generator1.fill_all()
print(generator1._level)"""