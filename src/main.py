from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    width = 800
    height = 600
    win = Window(width, height)

    cells = []
    cell_width = 40
    for i in range(0, width, cell_width):
        for j in range(0, height, cell_width):
            cells.append(Cell(win, i, j, i + cell_width, j + cell_width))
            print(f"Added cell: 'x1':{i} 'x2':{i+cell_width} 'y1':{j} 'y2'{j+cell_width}:")
    
    for cell in cells:
        if isinstance(cell, Cell):
            cell.draw("black")
    
    win.is_running = True
    print("Running!")
    win.wait_for_close()
    print("Closing...")

main()