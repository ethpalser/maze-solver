from window import Window
from maze import Maze

def main():
    width = 800
    height = 600
    win = Window(width, height)
    maze = Maze(100, 100, 12, 10, 40, 40, win)
    maze.solve()
    win.is_running = True # Keeps the window open
    win.wait_for_close()

main()