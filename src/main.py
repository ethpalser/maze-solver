from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    width = 800
    height = 600
    win = Window(width, height)
    maze = Maze(100, 100, 12, 12, 40, 40, win)
    
    win.is_running = True
    print("Running!")
    win.wait_for_close()
    print("Closing...")

main()