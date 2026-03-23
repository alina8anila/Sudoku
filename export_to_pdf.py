from reportlab.pdfgen import canvas as pdf_canvas
from classes.SudokuGrid import SudokuGrid

def export_pdf(grid :SudokuGrid):
    filename = "sudoku.pdf"
    pdf = pdf_canvas.Canvas(filename)

    pdf.setFont("Helvetica", 20)
    pdf.drawString(200, 800, "Sudoku Puzzle")

    cell: int =40
    x0: int =100
    y0: int =400
    gap: int =0
    for i in range(10):
        w: int = 2 if i % 3 != 0 else 4
        pdf.setLineWidth(w)
        pdf.line(x0+(i)*(gap+cell), y0, x0+(i)*(gap+cell), y0+9*(cell+gap))
        pdf.line(x0, y0+(i)*(gap+cell), x0+9*(cell+gap), y0+(i)*(gap+cell))

    x0+=10
    y0+=10

    pdf.setFont("Helvetica", 30)

    for i in range(1, 10):
        for j in range(1, 10):
            val = grid.cell[i][10-j].val
            if val != 0: pdf.drawString(x0+(i-1)*(gap+cell), y0+(j-1)*(gap+cell), str(val))

    pdf.save()